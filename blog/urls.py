from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
]
