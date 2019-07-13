from django.urls import path
from . import views

urlpatterns = [
	path('', views.blog, name="blog"),
	path('category/<int:category_id>/', views.category, name='category'), #int: makes sure that the characters will be numbers, otherwise it would be str
]