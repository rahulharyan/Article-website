from django.urls import path
from base import views

urlpatterns = [
    path('', views.base_home,name='home'),
    path('about' , views.about,name='about'),
    path('eduaction', views.eduaction,name='eduaction'),
    path('read/<str:pk>', views.read, name='read'),
    path('read_eduaction/<str:pk>', views.read_eduaction,name='read_eduaction'),
    path('social_media', views.social_media,name='social_media'),
    path('read_social_media/<str:pk>', views.read_social_media,name='read_social_media'),
    path('Business', views.business,name='business'),
    path('read_business/<str:pk>', views.read_business,name='read_business'),
    path('politics', views.politics,name='politics'),
    path('read_politics/<str:pk>', views.read_politics,name='read_politics'),
    path('goverment' , views.goverment , name='goverment'),
    path('read_goverment/<str:pk>', views.read_goverment,name='read_goverment'),
    path('economy',views.economy,name='economy'),
    path('read_economy/<str:pk>', views.read_economy,name='read_economy'),
    path('health',views.health,name='health'),
    path('read_health/<str:pk>', views.read_health,name='read_health'),
    path('crime',views.crime,name='crime'),
    path('read_crime/<str:pk>', views.read_crime,name='read_crime'),
]
