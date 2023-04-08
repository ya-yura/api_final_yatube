"""
API serializers
"""
import base64
from rest_framework.relations import SlugRelatedField
from rest_framework import serializers

from posts.models import User, Post, Comment, Group, Follow
from django.core.files.base import ContentFile


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for the 'GroupViewSet'."""

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    """Serializer for the 'GroupViewSet'."""

    user = SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        many=False,
        read_only=True,
    )

    following = SlugRelatedField(
        slug_field='username',
        many=False,
        queryset=User.objects.all(),
    )

    class Meta:
        model = Follow
        fields = '__all__'
        read_only_fields = ('user',)

    def validate(self, data):
        if Follow.objects.filter(user=self.context['request'].user,
                                 following=data['following']).exists():
            raise serializers.ValidationError('Already followed')

        if self.context['request'].user == data['following']:
            raise serializers.ValidationError('Cant follow yourself')
        return data
