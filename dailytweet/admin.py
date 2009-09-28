from django.contrib import admin

from dailytweet.models import DailyTweet

class DailyTweetAdmin(admin.ModelAdmin):
    date_hierarchy = 'publish_date'
    list_display = ('message', 'creation_time', 'publish_date', 'published_time')
    list_filter = ('creation_time', 'publish_date')
    ordering = ('published_time', 'publish_date', '-creation_time')

admin.site.register(DailyTweet, DailyTweetAdmin)

