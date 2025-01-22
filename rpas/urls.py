from django.urls import path
from . import views

urlpatterns =[ 
  
  path('rpa/list/', views.RpaListView.as_view(), name='rpa_list'),

  path('rpa/create/', views.RpaCreateView.as_view(), name='rpa_create'),

  path('rpa/<int:pk>/detail/', views.RpaDetailView.as_view(), name='rpa_detail'),

  path('rpa/<int:pk>/update/', views.RpaUpdateView.as_view(), name='rpa_update'),

  path('rpa/<int:pk>/delete/', views.RpaDeleteView.as_view(),name='rpa_delete'),

  #retorno do back-end e autenticações do front

  path('v1/rpas/', views.RpaCreateListAPIView.as_view(), name='rpa-create-list-api-view'),
  path('v1/rpas/<int:pk>/', views.RpaRetrieveUpdateDestroyAPIView.as_view(), name='rpa-detail-api-view')

 ]