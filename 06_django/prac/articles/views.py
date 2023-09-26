from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # 모든 게시글 정보 보여줘
    # Class.manager.QuerySet API
    # <QuerySet [Article Object(1), Article Object(2)]>
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)