import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import metrics
from django.http import HttpResponse


@login_required(login_url='/login')
def home(request):

    #gráfico no front
    horas_diarias_data = metrics.get_horas_diarias()
    quantidade_erros = metrics.get_erros_diarias()
    horas_mensais_by_rpa_data = metrics.get_horas_mensais_by_rpa()
    erros_mensais_by_rpa_data = metrics.get_erros_mensais_by_rpa()
    

    #métricas gerais front
    rpa_metrics = metrics.get_rpa_metrics()
    rpa_objects = metrics.get_rpa_object()


    context = {
        'rpa_metrics': rpa_metrics,
        'rpa_objects': rpa_objects,
        #gráficos do front
        'horas_diarias_data': json.dumps(horas_diarias_data),
        'quantidade_erros': json.dumps(quantidade_erros),
        'horas_mensais_by_rpa_data':json.dumps(horas_mensais_by_rpa_data),
        'erros_mensais_by_rpa_data':json.dumps(erros_mensais_by_rpa_data)
    }


    if not request.user.is_authenticated:
        return HttpResponse("Usuário não autenticado", status=403)
    
    else:
        
        return render(request, 'home.html', context)