from . import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about', views.about,name='about'),
    path('models', views.models,name='models'),
	path('house',views.house,name='house'),
	path('flower',views.flower,name='flower'),
]
