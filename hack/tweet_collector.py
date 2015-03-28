import twitter
import os
import time


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
            print tweet['coordinates'], tweet['text']
