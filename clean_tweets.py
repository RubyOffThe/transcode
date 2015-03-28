#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, json
from textblob import TextBlob


python_wiki = TextBlob("Python is a high-level, general-purpose programming language.")
testimonial1 = TextBlob("Textblob is amazingly simple to use. What great fun!")
testimonial2 = TextBlob("Textblob is horrible to use. That was awful!")


#print "Neutral sentiment: ", python_wiki.sentiment.polarity
#print "Positive sentiment: ", testimonial1.sentiment.polarity
#print "Negative sentiment: ", testimonial2.sentiment.polarity

test1 = ".@NaomiCeder & @Trans_Code Hackathon participants and volunteers - Have fun hacking today at @GoCardless! ❤ #trans_code"

## Example of the data structure we want to build:
##{"metadata": ["@NaomiCeder", "@Trans_Code"]
## "tweet": [list of words]}

DICT_ANALYSIS = {}

def remove_non_ascii(tweet_text):
    clean_tweet = re.sub(r'[^\x00-\x7f]+', '', tweet_text)
    return clean_tweet

def remove_punctuation(tweet_text):
    clean_tweet = re.sub('[%s]' % re.escape('!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~'), '', tweet_text)
    return clean_tweet


def get_twitter_info(tweet_text):
    t = tweet_text.split()
    mentions = [i for i in t if '\x40' in i]
    hashtags = [i for i in t if '\x23' in i]
    DICT_ANALYSIS['mentions'] = mentions
    DICT_ANALYSIS['hashtags'] = hashtags
    return DICT_ANALYSIS

def get_sentiment(tweet_text, DICT_ANALYSIS):
    tweet_sentiment = TextBlob(tweet_text)
    DICT_ANALYSIS['sentiment'] = tweet_sentiment.sentiment.polarity
    return DICT_ANALYSIS



if __name__ == "__main__":
    t = remove_non_ascii(test1)
    print "without ascii: ", t
    s = remove_punctuation(t)
    print "without punctuation: ", s
    d = get_twitter_info(s)
    print get_sentiment(t, d)
