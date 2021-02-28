from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import get_user_model
from django.db.models import Count

from core.models import (
    Follow, 
    Post, 
    Like, 
    Comment, 
    SavedPost
    )
from core.forms import PostCreateForm

User = get_user_model()
# Create your views here.
class HomeView(View):
    template_name = 'core/feed.html'
    form_class = PostCreateForm

    def get(self, request, *arga, **kwargs):
        form = self.form_class()
        all_posts = Post.objects.all()
        context = { 'form': form, 'all_posts': all_posts }
        return render(request, self.template_name, context=context)


class PostDetailView(View):
    template_name = 'core/post_detail.html'

    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('id')

        try:
            post_obj = Post.objects.get(pk=post_id)
        except Exception as e:
            return redirect(request.META.get('HTTP_REFERER'))

        try:
            Like.objects.get(user=request.user, post_id=post_id)
            liked_this_post = True
        except Exception as e:
            liked_this_post = False

        try:
            SavedPost.objects.get(user=request.user, post_id=post_id)
            post_saved = True
        except Exception as e:
            post_saved = False

        context = {
            'post': post_obj, 
            'liked_this_post': liked_this_post, 
            'post_saved': post_saved,
            }
            
        return render(request, self.template_name, context=context)


class PostCreatView(View):
    template_name = 'core/feed.html'
    form_class = PostCreateForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home_feed_view')
        else:
            context = { 'form': form }
            return render(request, self.template_name, context=context)


class PostDeleteView(View):

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        try:
            post_obj = Post.objects.get(pk=post_id)
        except Exception as e:
            pass

        if request.user == post_obj.user:
            post_obj.delete()

        return redirect(request.META.get('HTTP_REFERER'))


class PostSaveView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        
        try:
            post_obj = Post.objects.get(pk=post_id)
        except Exception as e:
            pass

        try:
            SavedPost.objects.create(post_id=post_id)
        except Exception as e:
            pass        

        return redirect(request.META.get('HTTP_REFERER'))


class PostUnsaveView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        
        try:
            savedpost_obj = SavedPost.objects.get(post_id=post_id)
            savedpost_obj.delete()
        except Exception as e:
            pass       

        return redirect(request.META.get('HTTP_REFERER'))


class PostLikeView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')

        try:
            Like.objects.get(user=request.user, post_id=post_id)
        except Exception as e:
            Like.objects.create(post_id=post_id)

        return redirect(request.META.get('HTTP_REFERER'))


class PostUnlikeView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')

        try:
            like_obj = Like.objects.get(user=request.user, post_id=post_id)
            like_obj.delete()
        except Exception as e:
            pass

        return redirect(request.META.get('HTTP_REFERER'))


class PostCommentView(View):
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('id')
        comment_text = request.POST.get('comment_text')
        
        Comment.objects.create(post_id=post_id, text=comment_text)

        return redirect(request.META.get('HTTP_REFERER'))


class FollowDoneView(View):
    def post(self, request, *args, **kwargs):
        followed_user_id = request.POST.get('followed_user_id')
        followed_user_obj = User.objects.get(pk=followed_user_id)

        try:
            Follow.objects.get(user=request.user, followed=followed_user_obj)
        except Exception as e:
            follow_obj = Follow.objects.create(followed=followed_user_obj)

        return redirect(request.META.get('HTTP_REFERER'))


class UnfollowDoneView(View):
    def post(self, request, *args, **kwargs):
        unfollowed_user_id = request.POST.get('unfollowed_user_id')
        unfollowed_user_obj = User.objects.get(pk=unfollowed_user_id)

        try:
            follow_obj = Follow.objects.get(user=request.user, followed=unfollowed_user_obj)
            follow_obj.delete()
        except Exception as e:
            pass

        return redirect(request.META.get('HTTP_REFERER'))


class LikedPostsView(View):
    template_name = 'core/liked_posts.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SavedPostsView(View):
    template_name = 'core/saved_posts.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ExplorePostsView(View):
    template_name = 'core/posts_explore.html'
    def get(self, request, *args, **kwargs):

        all_posts = Post.objects.annotate(count=Count('like')).order_by('-count')
        context = {'all_posts': all_posts}
        return render(request, self.template_name, context=context)