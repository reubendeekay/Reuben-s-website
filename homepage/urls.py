from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('',views.home,name="homepage"),
    path('new_search',views.new_search,name="new_search"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)