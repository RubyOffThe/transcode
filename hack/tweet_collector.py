import twitter
import os
import time
import threading
import re
from textblob import TextBlob
import logging
import sys

logger = logging.getLogger(__name__)
stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)

positivity = []
global_average_positivity = 0


class ProcessingThread(threading.Thread):

    def __init__(self, search_term):
        self.search_term = search_term
        super(ProcessingThread, self).__init__()

    def remove_non_ascii(tweet_text):
        clean_tweet = re.sub(r'[^\x00-\x7f]+', '', tweet_text)
        return clean_tweet

    def remove_punctuation(tweet_text):
        clean_tweet = re.sub('[%s]' % re.escape('!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~'), '', tweet_text)
        return clean_tweet

    def run(self):
        global positivity
        c = Collector()
        c.connect()
        for tweet in c.stream(self.search_term):
            text = tweet["text"]
            text = self.remove_non_ascii(text)
            text = self.remove_punctuation(text)
            print text

            blob = TextBlob(text)

            average_positivity = []
            total_positivity = 0

            for sentence in blob.sentences:
                average_positivity.append(sentence.sentiment.polarity)

            for value in average_positivity:
                total_positivity += value

            ret_val = total_positivity/len(average_positivity)
            logger.debug("%s -- %s", tweet['text'], ret_val)

            positivity.append(ret_val)


class Collector(object):

    def connect(self):
        self.ts = twitter.TwitterStream(
            auth=twitter.OAuth(
                os.environ['TWITTER_USER_TOKEN'],
                os.environ['TWITTER_USER_SECRET'],
                os.environ['TWITTER_ID'],
                os.environ['TWITTER_SECRET']
            )
        )

    def stream(self, search_term):
        try:
            atmosphere = self.ts.statuses.filter(track=search_term)
        except twitter.api.TwitterHTTPError:
            time.sleep(60 * 5)
            raise

        for tweet in atmosphere:
            yield tweet
