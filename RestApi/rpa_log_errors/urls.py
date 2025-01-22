from django.urls import path
from . import views

urlpatterns =[ 
  
  path('rpa_log_error/list/', views.RpaLogErrorListView.as_view(), name='rpa_log_error_list'),

  path('rpa_log_error/create/', views.RpaLogErrorCreateView.as_view(), name='rpa_log_error_create'),

  path('rpa_log_error/<int:pk>/detail/', views.RpaLogErrorDetailView.as_view(), name='rpa_log_error_detail'),

  path('rpa_log_error/<int:pk>/update/', views.RpaLogErrorUpdateView.as_view(), name='rpa_log_error_update'),

  path('rpa_log_error/<int:pk>/delete/', views.RpaLogErrorDeleteView.as_view(),name='rpa_log_error_delete'),

  #retorno da autenticação e back-end

  path('v1/rpa_error/',views.RpaLogErrorListAPIView.as_view(),name='rpaLogError-list-api-view'),
  path('v1/<int:pk>/', views.RpaLogErrorRetrieveUpdateDestroyAPIView.as_view(), name='rpaLogError-detail-api-view')


 ]

 