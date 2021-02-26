from django.urls import path
from core.views import (
    HomeView,
    FollowDoneView,
    UnfollowDoneView,
    )
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('feed/', login_required(HomeView.as_view()), name='home_feed_view'),

    # follow and unfollow view
    path('follow/done/', login_required(FollowDoneView.as_view()), name='follow_done_view'),
    path('unfollow/done/', login_required(UnfollowDoneView.as_view()), name='unfollow_done_view')
]