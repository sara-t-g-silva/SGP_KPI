from django.urls import path
from . import views

urlpatterns =[ 
  
  path('rpa_log_success/list/', views.RpaLogSuccessListView.as_view(), name='rpa_log_success_list'),

  path('rpa_log_success/create/', views.RpaLogSuccessCreateView.as_view(), name='rpa_log_success_create'),

  path('rpa_log_success/<int:pk>/detail/', views.RpaLogSuccessDetailView.as_view(), name='rpa_log_success_detail'),

  path('rpa_log_success/<int:pk>/update/', views.RpaLogSuccessUpdateView.as_view(), name='rpa_log_success_update'),

  path('rpa_log_success/<int:pk>/delete/', views.RpaLogSuccessDeleteView.as_view(),name='rpa_log_success_delete'),

  #retorno da autenticação e back-end

  path('v1/rpa_success/',views.RpaLogSuccessListAPIView.as_view(),name='rpaLogSuccess-list-api-view'),
  path('v1/<int:pk>/', views.RpaLogSuccessRetrieveUpdateDestroyAPIView.as_view(), name='rpaLogSuccess-detail-api-view')


 ]