from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# views 文件用于连接 models 和 templates
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) #用 render 方法渲染模板 blog/post_list.html 而得到的结果

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


