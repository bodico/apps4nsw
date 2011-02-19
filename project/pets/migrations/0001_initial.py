# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Animal'
        db.create_table('pets_animal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('colour', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('suburb', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('flavour', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('other', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('pets', ['Animal'])

        # Adding model 'Postcode'
        db.create_table('pets_postcode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal('pets', ['Postcode'])


    def backwards(self, orm):
        
        # Deleting model 'Animal'
        db.delete_table('pets_animal')

        # Deleting model 'Postcode'
        db.delete_table('pets_postcode')


    models = {
        'pets.animal': {
            'Meta': {'object_name': 'Animal'},
            'colour': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'flavour': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'other': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'pets.postcode': {
            'Meta': {'object_name': 'Postcode'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['pets']
