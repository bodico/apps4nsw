# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Animal.other'
        db.delete_column('pets_animal', 'other')

        # Deleting field 'Animal.name'
        db.delete_column('pets_animal', 'name')

        # Deleting field 'Animal.suburb'
        db.delete_column('pets_animal', 'suburb')

        # Deleting field 'Animal.colour'
        db.delete_column('pets_animal', 'colour')

        # Deleting field 'Animal.type'
        db.delete_column('pets_animal', 'type')

        # Adding field 'Animal.postcode'
        db.add_column('pets_animal', 'postcode', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.counter'
        db.add_column('pets_animal', 'counter', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'Animal.category_id'
        db.add_column('pets_animal', 'category_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'Animal.category_name'
        db.add_column('pets_animal', 'category_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Animal.other'
        db.add_column('pets_animal', 'other', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.name'
        db.add_column('pets_animal', 'name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.suburb'
        db.add_column('pets_animal', 'suburb', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.colour'
        db.add_column('pets_animal', 'colour', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True), keep_default=False)

        # Adding field 'Animal.type'
        db.add_column('pets_animal', 'type', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True), keep_default=False)

        # Deleting field 'Animal.postcode'
        db.delete_column('pets_animal', 'postcode')

        # Deleting field 'Animal.counter'
        db.delete_column('pets_animal', 'counter')

        # Deleting field 'Animal.category_id'
        db.delete_column('pets_animal', 'category_id')

        # Deleting field 'Animal.category_name'
        db.delete_column('pets_animal', 'category_name')


    models = {
        'pets.animal': {
            'Meta': {'object_name': 'Animal'},
            'category_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'counter': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'flavour': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
