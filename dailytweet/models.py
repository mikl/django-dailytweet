from datetime import datetime

from django.db import models
from django.db.models import Q
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

import twitter

class BigIntegerField(models.IntegerField):
    """
    Provide a model field for BigInts

    This is for whatever reason not included in Django, so we'll provide
    our own, since Twitter status IDs have long since crossed the limits
    for 32-bit integers.
    """
    empty_strings_allowed=False
    def get_internal_type(self):
        return "BigIntegerField"
    def db_type(self):
        return 'bigint' # Note this won't work with Oracle.


class DailyTweet(models.Model):
    message = models.CharField(max_length=140, help_text=_('Your Tweet message'))
    publish_date = models.DateField(null=True, blank=True, help_text=_('The date where this Tweet should be published. If empty, it will be published when there is none that matches current date.'))
    creation_time = models.DateTimeField(auto_now_add=True, editable=False)
    published_time = models.DateTimeField(null=True, blank=True,
                                          editable=False)
    status_id = BigIntegerField(null=True, blank=True, editable=False)

    def post_to_twitter(self):
        username = getattr(settings, 'TWITTER_USERNAME')
        password = getattr(settings, 'TWITTER_PASSWORD')

        if not username or not password:
            # Credentials not available, bail out.
            return False

        status = twitter.Api(username, password).PostUpdate(self.message)

        if status:
            self.status_id = status.id
            self.published_time = datetime.fromtimestamp(status.created_at_in_seconds)
            self.save()
            return status.id

    @classmethod
    def get_unposted(cls):
        """
        Get a single, unposted DailyTweet

        Only returns DailyTweets that are immidiately postable, if
        publish_date is null or current date.
        """
        now = datetime.now()

        # First, try to get one with a matching date.
        tweets = cls.objects.filter(publish_date=now.date(),
                                    status_id__isnull=True,
                                   ).order_by('creation_time')

        if tweets:
            return tweets[0]

        # Otherwise, get one without a publish_date.
        tweets = cls.objects.filter(publish_date__isnull=True,
                                    status_id__isnull=True,
                                   ).order_by('creation_time')

        if tweets:
            return tweets[0]
        return False

    def __unicode__(self):
        return 'DailyTweet: %s' % self.message

