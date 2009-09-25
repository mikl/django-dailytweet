from django.contrib import admin

from dailytweet.models import DailyTweet

class DailyTweetAdmin(admin.ModelAdmin):
    list_display = ('message', 'publish_date', 'published_time')

admin.site.register(DailyTweet, DailyTweetAdmin)

