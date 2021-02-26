from django.contrib import admin
from core.models import (
    Post, 
    Comment,
    Like,
    Follow,
)
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('text', 'image', 'user', 'created_on', 'updated_on')


class CommentModelAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('text', 'post', 'user', 'commented_on', 'updated_on')


class LikeModelAdmin(admin.ModelAdmin):
    model = Like
    list_display = ('post', 'user', 'is_like', 'liked_on', 'updated_on')


class FollowModelAdmin(admin.ModelAdmin):
    model = Follow
    list_display = ('user', 'followed', 'followed_on', 'updated_on')


admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
admin.site.register(Like, LikeModelAdmin)
admin.site.register(Follow, FollowModelAdmin)