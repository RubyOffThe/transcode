# -*- coding: utf-8 -*-
from mock import Mock

from ..tweet_collector import (
    Collector,
    remove_non_ascii,
    remove_punctuation,
    tweet_sentiment
)


def test_non_ascii_strips_the_non_ascii_set():
    assert remove_non_ascii('woah % ₤ 😸   no') == 'woah %     no'


def test_remove_punctuation():
    punctuated_string = 'this year; are, -- stay_ing,'

    assert remove_punctuation(punctuated_string) == 'this year are  staying'


def test_collector_stream_is_a_generator():
    c = Collector()
    c.ts = Mock()
    c.ts.statuses.filter.return_value = [1, 2, 3, 4]

    generator = c.stream('search term')

    assert list(generator) == [1, 2, 3, 4]
    assert c.ts.statuses.filter.call_args[1]['track'] == 'search term'


def test_tweet_sentiment_positive_tweet():
    positive_tweet = "You have to see this because it's amazing"

    assert tweet_sentiment(positive_tweet) == 0.6000000000000001


def test_tweet_sentiment_negative_tweet():
    negative_tweet = "Things are definitely over this time I hate it"

    assert tweet_sentiment(negative_tweet) == -0.4


def test_tweet_sentiment_empty_tweet():
    assert tweet_sentiment('') == None
