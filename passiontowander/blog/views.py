from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, HeadingContentBlock, TextContentBlock, UploadedImage, UploadedVideo
from .forms import PostForm, ImageForm, VideoForm

def home(request):
    posts = Post.objects.exclude(title="All Photos")[:3]
    return render(request, 'blog/home.html', {'posts': posts})


# View for the blog post list.
def post_list(request):
    # Get all blog posts.
    posts = Post.objects.all().prefetch_related('images')
    # Render the 'post_list.html' template with the posts context.
    return render(request, 'blog/post_list.html', {'posts': posts})


# View for creating a new blog post.
def post_create(request):
    if request.method == 'POST':
        p_form = PostForm(request.POST, request.FILES)
        i_form = ImageForm(request.POST, request.FILES)
        if p_form.is_valid() and i_form.is_valid():
            post = p_form.save(commit=False)
            post.author = request.user
            post.save()
            
            image = i_form.save(commit=False)
            image.post = post
            image.save()

            return redirect('post_detail', pk=post.pk)
    else:
        p_form = PostForm()
        i_form = ImageForm()
        
    return render(request, 'blog/post_edit.html', {'p_form': p_form, 'i_form': i_form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    heading_content_blocks = HeadingContentBlock.objects.filter(post=post).order_by('order')
    text_content_blocks = TextContentBlock.objects.filter(post=post).order_by('order')
    image_content_blocks = UploadedImage.objects.filter(post=post).order_by('order')
    video_content_blocks = UploadedVideo.objects.filter(post=post).order_by('order')

    all_blocks = list(heading_content_blocks) + list(text_content_blocks) + list(image_content_blocks) + list(video_content_blocks)
    all_blocks.sort(key=lambda block: block.order)

#    content_blocks = post.content_blocks.all()
#    heading_blocks = post.headingcontentblock_set.all()
#    text_blocks = post.textcontentblock_set.all()
#    image_blocks = post.imagecontentblock_set.all()
#    video_blocks = post.videocontentblock_set.all()

    # Combine all blocks into one list and sort by 'order'
#    content_blocks = sorted(
#        list(heading_blocks) + list(text_blocks) + list(image_blocks) + list(video_blocks),
#        key=lambda block: block.order
#    )

    return render(request, 'blog/post_detail.html', {'post': post, 'content_blocks': all_blocks})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/all-posts.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

# The following models are used indirectly by the upload forms
assert UploadedImage
assert UploadedVideo

def upload_image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the URL of the previous page
            previous_page = request.META.get('HTTP_REFERER')
            # Redirect to the previous page
            return redirect(previous_page)
    else:
        form = ImageForm()
    return render(request, 'blog/upload_image.html', {'form': form})

def upload_video_view(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            previous_page = request.META.get('HTTP_REFERER')
            return redirect(previous_page)
    else:
        form = VideoForm()
    return render(request, 'blog/upload_video.html', {'form': form})

def imprint(request):
    return render(request, 'blog/imprint.html')


def privacy_policy(request):
    return render(request, 'blog/privacy-policy.html')


def terms_and_conditions(request):
    return render(request, 'blog/terms-and-conditions.html')
