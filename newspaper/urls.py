
from django.urls import path
from . import views

urlpatterns = [
    path("news/", views.NewsModelListView.as_view(), name="news"),
    path("news/new", views.NewsFormView.as_view(), name="new"),
    path('news/<int:news_id>/edit', views.NewsFormEditView.as_view(), name='edit'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail')
]
