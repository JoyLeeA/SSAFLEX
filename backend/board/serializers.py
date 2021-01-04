from rest_framework import serializers
from .models import Article, Comment
from accounts.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        # ('id', 'title', 'content', 'created_at', 'updated_at',)


class CommentSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # ('article', 'id', 'content', 'created_at', 'updated_at',)
