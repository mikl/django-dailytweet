Django Daily Tweet
==================

A simple reusable app to post daily (or otherwise recurring) message to
Twitter. Useful for quote/tip of the day style of apps.

Installation
------------

1. Install the dailytweet app with `easy_install`, `python setup.py
   install`, `pip` or whatever method you prefer.
2. Use the example_project or install dailytweet into a project of your
   own.
3. Remember to set `TWITTER_USERNAME` and `TWITTER_PASSWORD` in your
   settings file (if using `example_project`, copy
   `local_settings.py.template` and edit it.
4. Run `manage.py syncdb` and add some DailyTweets in the interface.
5. Set up a cron job to run `manage.py post_daily_tweet` daily.
6. Profit.

