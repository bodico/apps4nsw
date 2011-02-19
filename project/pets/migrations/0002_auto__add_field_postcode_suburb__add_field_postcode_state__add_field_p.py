# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Postcode.suburb'
        db.add_column('pets_postcode', 'suburb', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True), keep_default=False)

        # Adding field 'Postcode.state'
        db.add_column('pets_postcode', 'state', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True), keep_default=False)

        # Adding field 'Postcode.dc'
        db.add_column('pets_postcode', 'dc', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True), keep_default=False)

        # Adding field 'Postcode.type'
        db.add_column('pets_postcode', 'type', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True), keep_default=False)

        # Adding field 'Postcode.lat'
        db.add_column('pets_postcode', 'lat', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True), keep_default=False)

        # Adding field 'Postcode.lon'
        db.add_column('pets_postcode', 'lon', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True), keep_default=False)

        # Changing field 'Postcode.postcode'
        db.alter_column('pets_postcode', 'postcode', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Animal.flavour'
        db.alter_column('pets_animal', 'flavour', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Animal.name'
        db.alter_column('pets_animal', 'name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Animal.colour'
        db.alter_column('pets_animal', 'colour', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Animal.suburb'
        db.alter_column('pets_animal', 'suburb', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Animal.other'
        db.alter_column('pets_animal', 'other', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Animal.type'
        db.alter_column('pets_animal', 'type', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))


    def backwards(self, orm):
        
        # Deleting field 'Postcode.suburb'
        db.delete_column('pets_postcode', 'suburb')

        # Deleting field 'Postcode.state'
        db.delete_column('pets_postcode', 'state')

        # Deleting field 'Postcode.dc'
        db.delete_column('pets_postcode', 'dc')

        # Deleting field 'Postcode.type'
        db.delete_column('pets_postcode', 'type')

        # Deleting field 'Postcode.lat'
        db.delete_column('pets_postcode', 'lat')

        # Deleting field 'Postcode.lon'
        db.delete_column('pets_postcode', 'lon')

        # User chose to not deal with backwards NULL issues for 'Postcode.postcode'
        raise RuntimeError("Cannot reverse this migration. 'Postcode.postcode' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Animal.flavour'
        raise RuntimeError("Cannot reverse this migration. 'Animal.flavour' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Animal.name'
        raise RuntimeError("Cannot reverse this migration. 'Animal.name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Animal.colour'
        raise RuntimeError("Cannot reverse this migration. 'Animal.colour' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Animal.suburb'
        raise RuntimeError("Cannot reverse this migration. 'Animal.suburb' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Animal.other'
        raise RuntimeError("Cannot reverse this migration. 'Animal.other' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Animal.type'
        raise RuntimeError("Cannot reverse this migration. 'Animal.type' and its values cannot be restored.")


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
