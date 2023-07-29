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
    path('tswifts/<int:tswift_id>/add_datinghistory/', views.add_datinghistory, name='add_datinghistory'),
    path('awards/', views.AwardList.as_view(), name='awards_index'),
    path('awards/<int:pk>/', views.AwardDetail.as_view(), name='awards_detail'),
    path('awards/create/', views.AwardCreate.as_view(), name='awards_create'),
    path('awards/<int:pk>/update/', views.AwardUpdate.as_view(), name='awards_update'),
    path('awards/<int:pk>/delete/', views.AwardDelete.as_view(), name='awards_delete'),
]