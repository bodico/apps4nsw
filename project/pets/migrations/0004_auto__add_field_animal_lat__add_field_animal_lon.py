# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Animal.lat'
        db.add_column('pets_animal', 'lat', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.lon'
        db.add_column('pets_animal', 'lon', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Animal.lat'
        db.delete_column('pets_animal', 'lat')

        # Deleting field 'Animal.lon'
        db.delete_column('pets_animal', 'lon')


    models = {
        'pets.animal': {
            'Meta': {'object_name': 'Animal'},
            'category_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'counter': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'flavour': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
        },
        'pets.postcode': {
            'Meta': {'object_name': 'Postcode'},
            'dc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['pets']
