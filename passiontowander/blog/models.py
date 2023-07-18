from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



def img_upload_to(instance, filename):
    # Generate file path
    return 'gallery_images/{}/{}/{}'.format(instance.country, instance.region, filename)


def vid_upload_to(instance, filename):
    # Generate file path
    return 'gallery_videos/{}/{}/{}'.format(instance.country, instance.region, filename)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='cover_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class ContentBlock(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, default=0)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        abstract = True  # Make this an abstract base class


class HeadingContentBlock(ContentBlock):
    heading = models.CharField(max_length=200)

    def __str__(self):
        return self.heading


class TextContentBlock(ContentBlock):
    content = models.TextField(default='')

    def __str__(self):
        return self.content[:50] + "..."  # Returns the first 50 characters followed by an ellipsis


#class ImageContentBlock(ContentBlock):
#    image = models.ImageField(upload_to=img_upload_to)
#    country = models.CharField(max_length=200, default='')  # adjust as needed
#    #region = models.CharField(max_length=200, default='')  # adjust as needed

#    def __str__(self):
#        return str(self.image)


#class VideoContentBlock(ContentBlock):
#    video = models.FileField(upload_to=vid_upload_to)
#    country = models.CharField(max_length=200, default='')  # adjust as needed
#    #region = models.CharField(max_length=200, default='')  # adjust as needed

#    def __str__(self):
#        return str(self.video)

class UploadedImage(ContentBlock):
    image = models.ImageField(upload_to=img_upload_to)
    country = models.CharField(max_length=100, default="")
    region = models.CharField(max_length=100, default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Image uploaded by {self.uploaded_by} at {self.uploaded_at}'

class UploadedVideo(ContentBlock):
    video = models.FileField(upload_to=vid_upload_to)
    country = models.CharField(max_length=100, default="")
    region = models.CharField(max_length=100, default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'Video uploaded by {self.uploaded_by} at {self.uploaded_at}'
