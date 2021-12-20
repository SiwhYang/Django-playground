from django.shortcuts import get_object_or_404, render ,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from cbv.models import Post,Comments
from django.contrib.auth.mixins import LoginRequiredMixin #和之前使用的登入login_required一樣但是是在cbv版本
from cbv.forms import PostForm
from cbv.forms import CommentForm

# Create your views here.


class Aboutview(TemplateView):  #如果template_name 沒有指定, django will infer object name eg: "books/publisher_list.html" when class name = PublisherListView
    template_name = 'about.html' # while template name will be lowercased most point 


class PostListView(ListView): #列出db的資料 類似查詢功能
    model = Post

    def get_queryset(self): #可以調用ORM 這個functipn在listview裡面本就有，可以被我們複寫
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):  #預設會取得url的pk並且去db撈出該筆資料
    model = Post

class CreatPostView(LoginRequiredMixin,CreateView): #重點 log繼承順序必須在左邊，一但使用該log 未經驗證的用戶請求都會被重導 or 404
    login_url = '/login/' #如果用戶沒有驗證會被導到這裏 by website:login_url就是匿名使用者訪問後重定向的url，一般都是login的頁面
    redirect_field_name = 'cbv/post_detail.html' #
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView): #logininrequiredMixin在cbv 就像在fbv使用@裝飾功能
    login_url = '/login/' #如果用戶沒有驗證會被導到這裏
    redirect_field_name = 'cbv/post_detail.html'
    form_class = PostForm #這個必須被import
    model = Post

class PostDeleteView(LoginRequiredMixin,DetailView):
    model = Post
    success_url = reverse_lazy('post_list') #這段是希望 等到delete結束後才導向

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/' #如果用戶沒有驗證會被導到這裏
    redirect_field_name = 'cbv/post_detail.html'
    model = Post
    def get_queryset(self): #可以調用ORM
        return Post.objects.filter(published_date__isnull=True.order_by('created_date'))
        #因為是草稿，所以條件是還沒有publish日期的


#########################
@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish
    return redirect('post_detail',pk=pk)


@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk) #這個會去調用get方法 找Post model裡pk=pk的data並存成post 如果找不到就顯示404
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save() #這段是要獲得form的資訊，但在真正save之前要做一些更動
            comment.post = post #先將comment的post和db裡面撈出來的post做連結
            comment.save() #再儲存
            return redirect('post_detail',pk=post.pk)
        else:
            form = CommentForm()
        return render (request,'cbv/comment_form.html',{'form':form})
    
@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comments,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)#要去找該comment對應的post的pk

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comments,pk=pk)
    post_pk = comment.post.pk #這段做的事是要先將pk存下來 不然下面刪掉之後 就找不到pk了
    comment.delete()
    return redirect('post_detail',pk=post_pk)
    