from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-pk')
        # serializer = TodoSerializer(todos, many=True)
        serializer = ArticleSerializer(articles, many=True)
        # print('content-----------------')
        # print(serializer.data)
        return Response(serializer.data)
    else:
        # print('aasdf')
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE', 'GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET': # detail
        # print('aaaa')
        serializer = ArticleSerializer(article)
        # serializer = ArticleSerializer(article, data=request.data)
        # print (serializer.data)
        return Response(serializer.data)
    # if not request.user.articles.filter(pk=article_pk).exists():
    #     return Response({'detail': '권한이 없습니다.'})
    if request.user == article.user:
        if request.method == 'PUT': # update
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        elif request.method == 'DELETE': # delete
            article.delete()
            return Response({ 'id': article_pk })
    else:
        print('권한이 없습니다.')
    


@api_view(['POST', 'GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comments_create_list(request, article_pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article)
            # print('asdf')
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        comments = Comment.objects.all().order_by('-pk')
        # serializer = TodoSerializer(todos, many=True)
        serializer = CommentSerializer(comments, many=True)
        # print('comment---------------')
        # print(serializer.data)
        return Response(serializer.data)



@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comments_delete(request, article_pk, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return Response({ 'id': comment_pk })

