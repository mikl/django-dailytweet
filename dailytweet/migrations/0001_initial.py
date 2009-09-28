
from south.db import db
from django.db import models
from dailytweet.models import *

class Migration:

    def forwards(self, orm):

        # Adding model 'DailyTweet'
        db.create_table('dailytweet_dailytweet', (
            ('id', orm['dailytweet.DailyTweet:id']),
            ('message', orm['dailytweet.DailyTweet:message']),
            ('publish_date', orm['dailytweet.DailyTweet:publish_date']),
            ('published_time', orm['dailytweet.DailyTweet:published_time']),
            ('status_id', orm['dailytweet.DailyTweet:status_id']),
        ))
        db.send_create_signal('dailytweet', ['DailyTweet'])

    def backwards(self, orm):

        # Deleting model 'DailyTweet'
        db.delete_table('dailytweet_dailytweet')


    models = {
        'dailytweet.dailytweet': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'published_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status_id': ('BigIntegerField', [], {'null': 'True', 'editable': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['dailytweet']
