from django.urls import path
from Rpa.views import (
    RpaCreateListView,
    RpaRetrieveUpdateDestroyView,
    RpaStaticsView,
    LogRpaCreateListView,
    LogRpaRetrieveUpdateDestroyView, 
    Log_rpa_error_model_CreateListView,
    Log_rpa_error_model_RetrieveUpdateDestroyView)


urlpatterns = [    
    
    path("",RpaCreateListView.as_view(), name ='rpa'),

    #path('rpa/<int:pk>', rpa_view_details, name="rpa_view_details")
    path('<int:pk>/', RpaRetrieveUpdateDestroyView.as_view(), name="rpa_view_details"),

    path('log/', LogRpaCreateListView.as_view(), name ='rpa_log'),

    path('log/<int:pk>/',LogRpaRetrieveUpdateDestroyView.as_view(), name='rpa_log_view_details'),

    path('log/error/', Log_rpa_error_model_CreateListView.as_view(), name ='rpa_log_erro'),

    path('log/error/<int:pk>/',Log_rpa_error_model_RetrieveUpdateDestroyView.as_view(), name='rpa_log_error_view_details'),
    
    path('statics/',RpaStaticsView.as_view(), name='statics_rpa_logs')
]