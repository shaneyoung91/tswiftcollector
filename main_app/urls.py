from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tswifts/', views.tswifts_index, name='tswifts'),
    path('tswifts/<int:tswift_id>/', views.tswifts_detail, name='detail'),
]