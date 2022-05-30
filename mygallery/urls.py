from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('search/', views.search_results, name='search_results'),
    path('category/<int:id>/', views.categoryPage, name='image-category'),
    path('category/<int:id>', views.imagePage, name='image-detail'),
]

