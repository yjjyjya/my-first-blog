from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {}) #用 render 方法渲染模板 blog/post_list.html 而得到的结果