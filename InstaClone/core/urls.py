from django.urls import path
from core.views import (
    HomeView,
    FollowDoneView,
    UnfollowDoneView,
    PostCreatView,
    PostDeleteView,
    )
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('feed/', login_required(HomeView.as_view()), name='home_feed_view'),

    # follow and unfollow view
    path('follow/done/', login_required(FollowDoneView.as_view()), name='follow_done_view'),
    path('unfollow/done/', login_required(UnfollowDoneView.as_view()), name='unfollow_done_view'),

    # post related urls
    path('post/create/', login_required(PostCreatView.as_view()), name='post_create_view'),
    path('post/delete/<int:id>', login_required(PostDeleteView.as_view()), name='post_delete_view')
]