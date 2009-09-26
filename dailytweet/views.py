from datetime import datetime, timedelta

from django.shortcuts import render_to_response
from django.template import RequestContext

from dailytweet.models import DailyTweet

def index(request):
    """
    Main index page, shows the last tweet with link to archive.
    """
    try:
        tweet = DailyTweet.objects.filter(status_id__isnull=False).order_by('-published_time')[0]
    except IndexError:
        tweet = False

    return render_to_response('front.html',
                              {'tweet': tweet},
                              context_instance=RequestContext(request))

