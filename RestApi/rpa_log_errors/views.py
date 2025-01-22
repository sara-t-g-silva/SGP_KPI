

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from . import models, forms, serializers
from rest_framework import generics

from rpas.models import Rpa

class RpaLogErrorListView(ListView):
    model = models.RpaLogError
    template_name = 'rpa_log_error_list.html'
    context_object_name = 'rpa_log_errors'
    #paginação dos registros
    paginate_by = 10
    permission_required = 'rpas.view_rpa_log_error'

    def get_queryset(self):
        queryset =  super().get_queryset()
        rpa = self.request.GET.get('rpa')


        if rpa:
            queryset = queryset.filter(rpa=rpa)

        return queryset
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rpas'] = Rpa.objects.all()
        return context
    

class RpaLogErrorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.RpaLogError
    template_name = 'rpa_log_error_create.html'
    form_class = forms.RpaLogErrorForm
    #redireciona para url que deseja, ao criar novo, retorna para a lista de rpas
    success_url = reverse_lazy('rpa_log_error_list')
    permission_required = 'rpa_log_errors.add_rpa_log_error'


class RpaLogErrorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.RpaLogError
    template_name = 'rpa_log_error_detail.html'
    permission_required = 'rpa_log_errors.view_rpa_log_error'


class RpaLogErrorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.RpaLogError
    template_name = 'rpa_log_error_update.html'
    form_class = forms.RpaLogErrorForm
    success_url = reverse_lazy('rpa_log_error_list')
    permission_required = 'rpa_log_errors.change_rpa_log_error'



class RpaLogErrorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model= models.RpaLogError
    template_name = 'rpa_log_error_delete.html'
    success_url=reverse_lazy('rpa_log_error_list')
    permission_required = 'rpa_log_errors.delete_rpa_log_error'


class RpaLogErrorListAPIView(generics.ListCreateAPIView):
    queryset = models.RpaLogError.objects.all()
    serializer_class = serializers.RpaLogErrorSerializer


class RpaLogErrorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.RpaLogError.objects.all()
    serializer_class = serializers.RpaLogErrorSerializer