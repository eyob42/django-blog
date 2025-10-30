from django.urls import path
from . import views
from typing import Any, cast

urlpatterns = [
    path("",views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<str:category>/", cast(Any, views.blog_category), name="blog_category"),
]