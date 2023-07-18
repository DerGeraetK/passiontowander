from django import forms
from .models import Post
from .models import UploadedImage, UploadedVideo

# Form for blog post creation.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'cover_image']

# Form for image uploading.
class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = UploadedImage
        fields = ['image', ]

#form for handling uploaded videos
class VideoForm(forms.ModelForm):
    class Meta:
        model = UploadedVideo
        fields = ['video']