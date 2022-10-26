from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    form = ArticleForm()
    if request.method == "POST":
        aform = ArticleForm(request.POST, request.FILES)
        if aform.is_valid():
            aform = aform.save(commit=False)
            aform.user = request.user
            aform.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('articles:index')
        else:
            form = ArticleForm()
    context = {
        "form" : form,
    }

    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment = CommentForm()
    context ={
        'article' : article,
        'comment': comment,
        'comments': article.comment_set.all(),
    }
    return render(request, 'articles/detail.html', context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance= article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    context = {
        'form' : form, 
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def comment(request, pk):
    article =get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.user = request.user
        messages.success(request, '댓글을 달았다.')
        comment.save()
        context = {
            'content': comment.content,
            'userName': comment.user.username
        }
    return JsonResponse(context)

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        messages.success(request, '댓글을 삭제했다.')
    return redirect('articles:detail', article_pk)

def search(request):
    search = request.GET.get("search")
    articles = Article.objects.filter(title__contains=search)
    context = {
        "articles" : articles,
    }
    return render(request, 'articles/index.html', context)


def comments_update (request,article_pk, comment_pk):
    pick_comment = Comment.objects.get(pk=comment_pk)
    pick_article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        C_Form = CommentForm(request.POST, instance=pick_comment )
        if C_Form.is_valid():
            a = C_Form (commit=False)
            a.article = pick_article    
            a.save()
            return redirect ("articles:index")
    return render(request,"articles/detail.html" ,)

@ login_required
def like(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,
    # if article.like_users.filter(id=request.user.id).exists():
    if request.user in article.like_users.all(): 
        # 좋아요 삭제하고
        article.like_users.remove(request.user)
        is_liked = False
    else:
        # 좋아요 추가하고 
        article.like_users.add(request.user)
        is_liked = True
    # 상세 페이지로 redirect
    context = {'isLiked': is_liked, 'likeCount': article.like_users.count()}
    return JsonResponse(context)