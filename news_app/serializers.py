from .models import NewsPost
from rest_framework import serializers


def post_serializer(post:NewsPost):
    return {
        'headline': post.headline,
        'content': post.content,
        'post_date': post.post_date
    }


class PostSerializer1(serializers.Serializer):
    headline = serializers.CharField(max_length=20)
    content = serializers.CharField(max_length=2000)
    post_date = serializers.DateTimeField()

    def create(self, validated_data):
        return NewsPost.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.headline = validated_data.get('headline', instance.headline)
        instance.content = validated_data.get('content', instance.content)
        instance.post_date = validated_data.get('post_date', instance.post_date)

        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=2000, required=False)

    class Meta:
        model = Post
        fields = "__all__"

