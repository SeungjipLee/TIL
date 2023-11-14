from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Post, Category
from .serializers import PostListSerializer, PostSerializer, CategorySerializer


# Create your views here.
@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def post_list_create(request):
    if request.method == 'GET':
        # 모든 post 정보를 요청자에게 넘겨준다.
        posts = Post.objects.all()
        # posts 리스트에 들어있는 각 post 정보들 중,
        # 사용자에게 넘겨줄 pk, title, content 정보만
        serializers = PostListSerializer(posts, many=True)
        # 정리한 dict 자료를 JSON로 변환하여 반환해야 한다.
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def post_detail(request, post_pk):
    # 일반적인 pk기준 조회
    post = get_object_or_404(Post, pk=post_pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)
