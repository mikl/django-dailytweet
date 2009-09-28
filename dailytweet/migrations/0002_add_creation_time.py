"""
Migration to add a creation_time field to the DailyTweet model.
"""

import datetime
from south.db import db
from django.db import models
from dailytweet.models import *


class Migration:
    def forwards(self, orm):
        # Temporarily assign a default value, since this column is not
        # nullable, and cannot be added without one.
        field = orm['dailytweet.dailytweet:creation_time']
        field.default = datetime.datetime.now()

        # Adding field 'DailyTweet.creation_time'
        db.add_column('dailytweet_dailytweet', 'creation_time', field, keep_default=False)



    def backwards(self, orm):
        # Deleting field 'DailyTweet.creation_time'
        db.delete_column('dailytweet_dailytweet', 'creation_time')


    models = {
        'dailytweet.dailytweet': {
            'creation_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'published_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status_id': ('BigIntegerField', [], {'null': 'True', 'editable': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['dailytweet']
