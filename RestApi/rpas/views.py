from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from . import models, serializer

from rest_framework import generics


from rpas.models import Rpa
from rpas.forms import RpaForm
from app import metrics



class RpaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Rpa
    template_name = 'rpa_list.html'
    context_object_name = 'rpas'
    #paginação dos registros
    paginate_by = 10
    permission_required = 'rpas.view_rpa'

    def get_queryset(self):
        queryset =  super().get_queryset()

        name = self.request.GET.get('name')
        status = self.request.GET.get('rpa_status')

        if name:
            #icontains é para que consiga filtrar por uma parte do nome, posso utilizar a mesma lógica para criar filtros de números por exemplo. 
            queryset = queryset.filter(name__icontains=name)

        if status:
            queryset = queryset.filter(rpa_status=status)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rpa_metrics'] = metrics.get_rpa_metrics()
        return context

    

class RpaCreateView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = Rpa
    template_name = 'rpa_create.html'
    form_class = RpaForm
    #redireciona para url que deseja, ao criar novo, retorna para a lista de rpas
    success_url = reverse_lazy('rpa_list')
    permission_required = 'rpas.add_rpa'


class RpaDetailView(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model = Rpa
    template_name = 'rpa_detail.html'
    permission_required = 'rpas.view_rpa'


class RpaUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model = Rpa
    template_name = 'rpa_update.html'
    form_class = RpaForm
    success_url = reverse_lazy('rpa_list')
    permission_required = 'rpas.change_rpa'



class RpaDeleteView(LoginRequiredMixin, PermissionRequiredMixin,DeleteView):
    model=Rpa
    template_name = 'rpa_delete.html'
    success_url=reverse_lazy('rpa_list')
    permission_required = 'rpas.delete_rpa'
   

class RpaCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Rpa.objects.all()
    serializer_class = serializer.RpaSerializer


class RpaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Rpa.objects.all()
    serializer_class = serializer.RpaSerializer


