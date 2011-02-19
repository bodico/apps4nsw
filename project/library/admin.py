from django.contrib import admin
from settings import ADMIN_MEDIA_URL

class TinymceAdmin(admin.ModelAdmin):
    class Media:
        js = (
            ADMIN_MEDIA_URL + 'tinymce/jscripts/tiny_mce/tiny_mce.js', 
            ADMIN_MEDIA_URL + 'tinymce_setup/tinymce_setup.js',
         )

class OrderedInline(admin.TabularInline):
    sortable_field_name = 'order'
    extra = 0
    