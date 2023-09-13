from django.shortcuts import render

# Create your views here.
def index(request):
    # render 함수가 하는 일?
    return render(request, 'articles/index.html')