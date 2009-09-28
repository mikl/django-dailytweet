"""
Unit tests for the dailytweet Django app.
"""
from datetime import datetime
from django.test import TestCase

from dailytweet.models import DailyTweet

class DailyTweetTestCase(TestCase):
    """
    Tests for the DailyTweet model.
    """
    fixtures = ['test_dailytweets']
    def test_get_unposted(self):
        """
        Test the get_unposted method.

        Make sure that get_unposted returns the most relevant tweet,
        preferring those that have a matching publish_date to those
        that have no publish_date. Those that have a non-matching
        publish_date set should not be considered.
        """
        now = datetime.now()
        tweets = []

        # Let's add some more tweets for testing.
        tweets.append(DailyTweet(message="TestTweet 0"))
        tweets.append(DailyTweet(message="TestTweet 1", publish_date=now.date()))
        tweets.append(DailyTweet.objects.create(message="TestTweet 2"))
        tweets.append(DailyTweet(message="TestTweet 3"))
        tweets.append(DailyTweet.objects.create(message="TestTweet 4", publish_date=now.date()))

        # Note that some of our Tweets were saved on creation, so their
        # IDs will be out of order (which is exactly what we want here)
        for tweet in tweets:
            tweet.save()
            print "ID: %d, Time: %s, Msg: %s" % (tweet.id, tweet.creation_time, tweet.message)

        # Here we should get "TestTweet 4", since it is the first one
        # added to the database that matches our date.
        t4 = DailyTweet.get_unposted()
        self.assertEqual(t4.id, tweets[4].id)

        # Set status_id and published_time to bogus values so that this
        # tweet is filtered out from the next get_unposted.
        t4.status_id = 25235
        t4.published_time = now
        t4.save()

        # Next should be "TestTweet 1", since thats the next with a
        # matching publish_date.
        t1 = DailyTweet.get_unposted()
        self.assertEqual(t1.id, tweets[1].id)

