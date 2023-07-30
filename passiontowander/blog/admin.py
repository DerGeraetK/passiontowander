from django.contrib import admin
from .models import Post, HeadingContentBlock, TextContentBlock, UploadedVideo, UploadedImage, ScriptContentBlock

class HeadingContentBlockAdmin(admin.StackedInline):
    model = HeadingContentBlock

class TextContentBlockAdmin(admin.StackedInline):
    model = TextContentBlock

class ScriptContentBlockAdmin(admin.StackedInline):
    model = ScriptContentBlock
#    extra = 1               # specifies how many empty forms are displayed for this inline.

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
        ScriptContentBlockAdmin,        
        UploadedImageAdmin,
        UploadedVideoAdmin,
#        ImageContentBlockAdmin,
#        VideoContentBlockAdmin,
    ]

admin.site.register(Post, PostAdmin)
