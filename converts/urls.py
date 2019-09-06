from django.urls import path

from .views import converter, HomePageView, CreatePostView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add/', CreatePostView.as_view(), name='add'),
]
