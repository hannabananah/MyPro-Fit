from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentListSerializer, CommentSerializer
from .models import Article, Comment

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def articles(req):
    if req.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif req.method == 'POST':
        serializer = ArticleListSerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=req.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def article_detail(req,article_pk):
    article=get_object_or_404(Article,pk=article_pk)
    if req.method=='GET':
        serializer=ArticleSerializer(article)
        return Response(serializer.data)
    
    elif req.method=='PUT':
        serializer=ArticleSerializer(article,data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    
    elif req.method=='DELETE':
        article.delete()
        data={
            'delete':f'게시글 {article_pk}번이 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def comments(req, article_pk):
    if req.method=='GET':
        article = get_object_or_404(Article, pk=article_pk)
        comment=get_list_or_404(Comment, article=article)
        serializer=CommentListSerializer(comment, many=True)
        return Response(serializer.data)
    elif req.method=='POST':
        article = get_object_or_404(Article, pk=article_pk)
        serializer=CommentListSerializer(data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=req.user, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def comment(req, article_pk, comment_pk):
    if req.method == 'PUT':
        comment = get_object_or_404(Comment, article__id=article_pk, pk=comment_pk)
        serializer = CommentSerializer(comment, data=req.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    elif req.method == 'DELETE':
        comment = get_object_or_404(Comment, article__id=article_pk, pk=comment_pk)
        comment.delete()
        data = {
            'delete': f'코멘트 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
