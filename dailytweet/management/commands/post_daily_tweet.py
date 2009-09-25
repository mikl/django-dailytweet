from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = "Posts the next available DailyTweet to Twitter"

    def handle_noargs(self, **options):
        from dailytweet.models import DailyTweet

        verbosity = int(options.get('verbosity', 1))

        tweet = DailyTweet.get_unposted()

        if verbosity >= 2:
            print "Posting DailyTweet %s" % tweet

        tweet.post_to_twitter()


