from django.contrib import admin
from .models import FilesCollect

# sent the thus created model to admin site
admin.site.register(FilesCollect)
# class FilesCollect(admin.ModelAdmin):
#     list_display=['id','url_text','img_upload']