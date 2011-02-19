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
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('colour', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('suburb', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('flavour', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('other', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('pets', ['Animal'])

        # Adding model 'Postcode'
        db.create_table('pets_postcode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('suburb', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('dc', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
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
            'colour': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'flavour': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'other': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
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
