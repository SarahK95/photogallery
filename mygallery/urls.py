from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.home,name = 'home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^category/<int:id>', views.categoryPage, name='image-category'),
    url(r'^category/<int:id>', views.imagePage, name='image-detail'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)