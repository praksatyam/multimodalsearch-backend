# content_management/models.py
from django.db import models

class ContentItem(models.Model):
    """
    A base class for all content items, storing the actual file in S3.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    # Store the actual file in S3 using Django's FileField
    file = models.FileField(upload_to='content_items/')

    # Store a reference to the vector embedding
    embedding_id = models.CharField(max_length=255, unique=True, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class TextDocument(ContentItem):
    """
    Represents a searchable text document like a PDF or Word file.
    """
    extracted_text = models.TextField(blank=True)

class Video(ContentItem):
    """
    Represents a video file.
    """
    duration_seconds = models.PositiveIntegerField(blank=True, null=True)
    transcript = models.TextField(blank=True)

class Image(ContentItem):
    """
    Represents an image file.
    """
    ocr_text = models.TextField(blank=True)

class LectureNote(ContentItem):
    """
    Represents general-purpose lecture notes.
    """
    content = models.TextField()

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)