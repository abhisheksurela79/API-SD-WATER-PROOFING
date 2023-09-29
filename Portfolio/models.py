from django.core.exceptions import ValidationError
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.validators import FileExtensionValidator



video_validator = FileExtensionValidator(["MP4", "WebM", "Ogg"])
pdf_validator = FileExtensionValidator(["PDF"])


def generate_thumbnail(field, size, quality):
    # Generate and save the thumbnail and small thumbnail from the provided image in thumbnail field
    # and small thumbnail field
    img = Image.open(field)
    img.thumbnail(size)
    thumb_io = BytesIO()
    img.save(thumb_io, format='JPEG', quality=quality)
    return thumb_io.getvalue()


class Images(models.Model):
    heading = models.CharField(max_length=50)
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/source images')
    thumbnail = models.ImageField(upload_to='photos/thumbnails/', blank=True, null=True)
    thumbnail_small = models.ImageField(upload_to='photos/small thumbnails/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate and save the thumbnail from the provided image in thumbnail field
        if not self.thumbnail:
            thumb = generate_thumbnail(self.image, size=(700, 700), quality=90)

            self.thumbnail = SimpleUploadedFile(
                f"{self.image.name.split('.')[0]}_thumbnail.jpg",
                thumb,
                content_type='image/jpeg'
            )

            thumb_sm = generate_thumbnail(self.image, size=(100, 100), quality=90)

            self.thumbnail_small = SimpleUploadedFile(
                f"{self.image.name.split('.')[0]}_thumbnail_small.jpg",
                thumb_sm,
                content_type='image/jpeg'
            )

            super().save(*args, **kwargs)

        else:
            thumb = generate_thumbnail(self.image, size=(100, 100), quality=90)

            self.thumbnail_small = SimpleUploadedFile(
                f"{self.thumbnail.name.split('.')[0]}_small.jpg",
                thumb,
                content_type='image/jpeg'
            )

            super().save(*args, **kwargs)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = "Images"



class Videos(models.Model):
    heading = models.CharField(max_length=50)
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/source videos', validators=[video_validator])
    thumbnail = models.ImageField(upload_to='videos/thumbnails/')
    thumbnail_small = models.ImageField(upload_to='videos/small thumbnails/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.thumbnail and not self.thumbnail_small:
            thumb = generate_thumbnail(self.thumbnail, size=(100, 100), quality=90)

            self.thumbnail_small = SimpleUploadedFile(
                f"{self.thumbnail.name.split('.')[0]}_small.jpg",
                thumb,
                content_type='image/jpeg'
            )

            super().save(*args, **kwargs)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = "Videos"



class PDF(models.Model):
    heading = models.CharField(max_length=50)
    caption = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdf/source pdf', validators=[pdf_validator])
    thumbnail = models.ImageField(upload_to='pdf/thumbnails/')
    thumbnail_small = models.ImageField(upload_to='pdf/small thumbnails/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.thumbnail and not self.thumbnail_small:
            thumb = generate_thumbnail(self.thumbnail, size=(100, 100), quality=90)

            self.thumbnail_small = SimpleUploadedFile(
                f"{self.thumbnail.name.split('.')[0]}_small.jpg",
                thumb,
                content_type='image/jpeg'
            )

            super().save(*args, **kwargs)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural = "PDF"

