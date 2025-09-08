from django.contrib import admin

# Register your models here.

# Register ContentItem subclasses for admin interface
from .models import TextDocument, Video, Image, LectureNote, UploadedFile

admin.site.register(TextDocument)
admin.site.register(Video)
admin.site.register(Image)
admin.site.register(LectureNote)
admin.site.register(UploadedFile)
