# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()

user_orm_label = '%s.%s' % (User._meta.app_label, User._meta.object_name)
user_model_label = '%s.%s' % (User._meta.app_label, User._meta.module_name)
user_ptr_name = '%s_ptr' % User._meta.object_name.lower()

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'AccessToken.user'
        db.alter_column('djoauth2_accesstoken', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm[user_orm_label], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'AccessToken.user'
        raise RuntimeError("Cannot reverse this migration. 'AccessToken.user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'AccessToken.user'
        db.alter_column('djoauth2_accesstoken', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm[user_orm_label]))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        user_model_label: {
            'Meta': {'object_name': User.__name__, 'db_table': "'%s'" % User._meta.db_table},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'djoauth2.accesstoken': {
            'Meta': {'object_name': 'AccessToken'},
            'authorization_code': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'access_tokens'", 'null': 'True', 'to': "orm['djoauth2.AuthorizationCode']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djoauth2.Client']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invalidated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lifetime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '3600'}),
            'refresh_token': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': "'S7EpB5SgVWGRP1mOYASLhP46m51sJV'", 'max_length': '30', 'blank': 'True', 'unique': 'True', 'db_index': 'True'}),
            'refreshable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'scopes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'access_tokens'", 'symmetrical': 'False', 'to': "orm['djoauth2.Scope']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['%s']" % user_orm_label, 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'default': "'j3bsoD5dhf4h5UYynJ358BX0B_4ll8'", 'unique': 'True', 'max_length': '30', 'db_index': 'True'})
        },
        'djoauth2.authorizationcode': {
            'Meta': {'object_name': 'AuthorizationCode'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djoauth2.Client']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invalidated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lifetime': ('django.db.models.fields.PositiveIntegerField', [], {'default': '600'}),
            'redirect_uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'scopes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'authorization_codes'", 'symmetrical': 'False', 'to': "orm['djoauth2.Scope']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['%s']" % user_orm_label}),
            'value': ('django.db.models.fields.CharField', [], {'default': "'V1i-2Tfbz.cKbivDa7PLFVLKaJBH3c'", 'unique': 'True', 'max_length': '30', 'db_index': 'True'})
        },
        'djoauth2.client': {
            'Meta': {'object_name': 'Client'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'default': "'AGZgLbyMY9l~GTuWKQNsMDi3eFwpCl'", 'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'redirect_uri': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'secret': ('django.db.models.fields.CharField', [], {'default': "'X1xv~~XjAt5AHh~rU9xu1dY8Ufm5v3'", 'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['%s']" % user_orm_label})
        },
        'djoauth2.scope': {
            'Meta': {'object_name': 'Scope'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256', 'db_index': 'True'})
        }
    }

    complete_apps = ['djoauth2']