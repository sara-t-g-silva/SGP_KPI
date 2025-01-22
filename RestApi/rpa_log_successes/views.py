

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from . import models, forms, serializers
from rest_framework import generics

from rpas.models import Rpa

class RpaLogSuccessListView(ListView):
    model = models.RpaLogSuccess
    template_name = 'rpa_log_success_list.html'
    context_object_name = 'rpa_log_successes'
    #paginação dos registros
    paginate_by = 10
    permission_required = 'rpas.view_rpa_log_success'

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
    

class RpaLogSuccessCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.RpaLogSuccess
    template_name = 'rpa_log_success_create.html'
    form_class = forms.RpaLogSuccessForm
    #redireciona para url que deseja, ao criar novo, retorna para a lista de rpas
    success_url = reverse_lazy('rpa_log_success_list')
    permission_required = 'rpa_log_successes.add_rpa_log_success'


class RpaLogSuccessDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.RpaLogSuccess
    template_name = 'rpa_log_success_detail.html'
    permission_required = 'rpa_log_successes.view_rpa_log_success'


class RpaLogSuccessUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.RpaLogSuccess
    template_name = 'rpa_log_success_update.html'
    form_class = forms.RpaLogSuccessForm
    success_url = reverse_lazy('rpa_log_success_list')
    permission_required = 'rpa_log_successes.change_rpa_log_success'



class RpaLogSuccessDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model= models.RpaLogSuccess
    template_name = 'rpa_log_success_delete.html'
    success_url=reverse_lazy('rpa_log_success_list')
    permission_required = 'rpa_log_successes.delete_rpa_log_success'


class RpaLogSuccessListAPIView(generics.ListCreateAPIView):
    queryset = models.RpaLogSuccess.objects.all()
    serializer_class = serializers.RpaLogSuccessSerializer


class RpaLogSuccessRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.RpaLogSuccess.objects.all()
    serializer_class = serializers.RpaLogSuccessSerializer