from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tswifts/', views.tswifts_index, name='index'),
    path('tswifts/<int:tswift_id>/', views.tswifts_detail, name='detail'),
    path('tswifts/create/', views.TSwiftCreate.as_view(), name='tswifts_create'),
    path('tswifts/<int:pk>/update/', views.TSwiftUpdate.as_view(), name='tswifts_update'),
    path('tswifts/<int:pk>/delete/', views.TSwiftDelete.as_view(), name='tswifts_delete'),
]