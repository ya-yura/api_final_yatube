"""
Posts DataBase model
"""

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """
    Posts Group DataBase model
    """
    title = models.CharField(
        verbose_name='Group name',
        help_text='Put group name here',
        max_length=200)
    slug = models.SlugField(
        verbose_name='Group slug',
        help_text='Put group slug here',
        unique=True)
    description = models.TextField(
        verbose_name='Group description',
        help_text='Put group description here'
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    Post DataBase model
    """

    text = models.TextField(
        verbose_name='Post text',
        help_text='Put post text here'
    )

    pub_date = models.DateTimeField(
        verbose_name='Post publish date',
        auto_now_add=True
    )

    author = models.ForeignKey(
        User,
        related_name='posts',
        verbose_name='Post author',
        on_delete=models.CASCADE,
    )

    group = models.ForeignKey(
        Group,
        related_name='posts',
        verbose_name='Post Group',
        help_text='Choose post group',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    image = models.ImageField(
        verbose_name='Post image',
        help_text='Choose post image',
        upload_to='posts/',
        blank=True,
        null=True
    )

    class Meta:
        """
        Post Meta
        """
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.text


class Comment(models.Model):
    """
    Comment DataBase model
    """

    author = models.ForeignKey(
        User,
        verbose_name='Comment author',
        related_name='comments',
        on_delete=models.CASCADE,
    )

    post = models.ForeignKey(
        Post,
        verbose_name='Commented post',
        related_name='comments',
        help_text='Comment text',
        on_delete=models.CASCADE,
    )

    text = models.TextField(
        verbose_name='Comment text',
        help_text='Put comment text here'
    )

    created = models.DateTimeField(
        verbose_name='Comment created',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        """
        Comment Meta
        """
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Follow(models.Model):
    """
    Follow DataBase model
    """

    user = models.ForeignKey(
        User,
        related_name='follower',
        verbose_name='Follower',
        on_delete=models.CASCADE,
    )

    following = models.ForeignKey(
        User,
        related_name='following',
        verbose_name='Following user',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.following
