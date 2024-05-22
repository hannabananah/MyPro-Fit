from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    # username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')
        read_only_fields = ('user',)


class ArticleSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
        

class CommentListSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ('id', 'comment_content', 'username')
        read_only_fields = ('user', 'username')

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'article', 'username')