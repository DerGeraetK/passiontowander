from django.contrib import admin
from .models import Post, HeadingContentBlock, TextContentBlock, UploadedVideo, UploadedImage

class HeadingContentBlockAdmin(admin.StackedInline):
    model = HeadingContentBlock

class TextContentBlockAdmin(admin.StackedInline):
    model = TextContentBlock

#class ImageContentBlockAdmin(admin.StackedInline):
#    model = ImageContentBlock

#class VideoContentBlockAdmin(admin.StackedInline):
#    model = VideoContentBlock

class UploadedVideoAdmin(admin.StackedInline):
    model = UploadedVideo

class UploadedImageAdmin(admin.StackedInline):
    model = UploadedImage

class PostAdmin(admin.ModelAdmin):
    inlines = [
        HeadingContentBlockAdmin,
        TextContentBlockAdmin,
        UploadedImageAdmin,
        UploadedVideoAdmin,
#        ImageContentBlockAdmin,
#        VideoContentBlockAdmin,
    ]

admin.site.register(Post, PostAdmin)
