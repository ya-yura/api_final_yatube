"""
API serializers
"""

from rest_framework.relations import SlugRelatedField
from rest_framework import serializers

from posts.models import User, Post, Comment, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

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
