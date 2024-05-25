from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    nickname = serializers.ReadOnlyField(source='user.nickname')
    class Meta:
        model = Article
        fields = ('id', 'title', 'content','nickname')
        read_only_fields = ('user','nickname')


class ArticleSerializer(serializers.ModelSerializer):
    nickname = serializers.ReadOnlyField(source='user.nickname')
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user','nickname')
        

class CommentListSerializer(serializers.ModelSerializer):
    nickname = serializers.ReadOnlyField(source='user.nickname')
    class Meta:
        model = Comment
        fields = ('id', 'comment_content','nickname')
        read_only_fields = ('user','nickname')

class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.ReadOnlyField(source='user.nickname')
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'article','nickname')