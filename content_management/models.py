# content_management/models.py
from django.db import models

class ContentItem(models.Model):
    """
    An abstract base class for all content items.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    # Store the path to the original file in S3. This is our source of truth.
    s3_key = models.CharField(max_length=512, unique=True)
    
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
    # Text will be extracted and stored here or in a separate field.
    # For a large project, you may store this text in a separate index.
    # For now, let's keep it simple.
    extracted_text = models.TextField(blank=True)

class Video(ContentItem):
    """
    Represents a video file.
    """
    duration_seconds = models.PositiveIntegerField(blank=True, null=True)
    
    # You might also want a field to store a transcript
    transcript = models.TextField(blank=True)

class Image(ContentItem):
    """
    Represents an image file.
    """
    # You can store OCR text from the image here.
    ocr_text = models.TextField(blank=True)

class LectureNote(ContentItem):
    """
    Represents general-purpose lecture notes.
    """
    content = models.TextField()