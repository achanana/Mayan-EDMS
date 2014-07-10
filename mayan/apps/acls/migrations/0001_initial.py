# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AccessEntry'
        db.create_table(u'acls_accessentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('permission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['permissions.StoredPermission'])),
            ('holder_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='access_holder', to=orm['contenttypes.ContentType'])),
            ('holder_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='object_content_type', to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'acls', ['AccessEntry'])

        # Adding model 'DefaultAccessEntry'
        db.create_table(u'acls_defaultaccessentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('permission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['permissions.StoredPermission'])),
            ('holder_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='default_access_entry_holder', to=orm['contenttypes.ContentType'])),
            ('holder_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='default_access_entry_class', to=orm['contenttypes.ContentType'])),
        ))
        db.send_create_signal(u'acls', ['DefaultAccessEntry'])

        # Adding model 'CreatorSingleton'
        db.create_table(u'acls_creatorsingleton', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lock_id', self.gf('django.db.models.fields.CharField')(default='1', unique=True, max_length=1)),
        ))
        db.send_create_signal(u'acls', ['CreatorSingleton'])


    def backwards(self, orm):
        # Deleting model 'AccessEntry'
        db.delete_table(u'acls_accessentry')

        # Deleting model 'DefaultAccessEntry'
        db.delete_table(u'acls_defaultaccessentry')

        # Deleting model 'CreatorSingleton'
        db.delete_table(u'acls_creatorsingleton')


    models = {
        u'acls.accessentry': {
            'Meta': {'object_name': 'AccessEntry'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'object_content_type'", 'to': u"orm['contenttypes.ContentType']"}),
            'holder_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'holder_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'access_holder'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['permissions.StoredPermission']"})
        },
        u'acls.creatorsingleton': {
            'Meta': {'object_name': 'CreatorSingleton'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lock_id': ('django.db.models.fields.CharField', [], {'default': "'1'", 'unique': 'True', 'max_length': '1'})
        },
        u'acls.defaultaccessentry': {
            'Meta': {'object_name': 'DefaultAccessEntry'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'default_access_entry_class'", 'to': u"orm['contenttypes.ContentType']"}),
            'holder_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'holder_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'default_access_entry_holder'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['permissions.StoredPermission']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'permissions.storedpermission': {
            'Meta': {'ordering': "('namespace',)", 'unique_together': "(('namespace', 'name'),)", 'object_name': 'StoredPermission'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'namespace': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['acls']