from django.utils import timezone
from django.db.models import Sum, F
from django.db.models.functions import ExtractMonth, ExtractYear
from django.db.models import Count

from datetime import timedelta

from rpas.models import Rpa
from rpa_log_successes.models import RpaLogSuccess
from rpa_log_errors.models import RpaLogError


def get_rpa_metrics():
   
    rpas = Rpa.objects.all()
    rpaLogSuccess = RpaLogSuccess.objects.all()

    rpa_running = sum(rpa.rpa_status=='running' for rpa in rpas)
    rpa_stopped = sum(rpa.rpa_status=='stopped' for rpa in rpas)
    #total de tempo de todos os rpas rodando no sistema.
    tempo_total = sum(rpa.duration.total_seconds() for rpa in rpas )
    total_erros = sum(rpa.error_count for rpa in rpas)

    def format_duration(seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
    
    formatted_time = format_duration(tempo_total)

    return dict(
        rpa_running=rpa_running,
        rpa_stopped=rpa_stopped,
        tempo_total=formatted_time,
        total_erros=total_erros
    )

def get_rpa_object():

    rpas = Rpa.objects.all()  # Obtém todos os objetos RPA

    if not rpas.exists():
        return []  # Retorna uma lista vazia se não houver objetos

    # Exemplo de retorno dos dados
    data = []
    for rpa in rpas:
        data.append({
            'name': rpa.name,
            'tempo_total': rpa.duration,
            'total_erros': rpa.error_count,
            'status': rpa.rpa_status,
        })

    return data

#retorna a soma dos últimos 7 dias
def get_horas_diarias():
    today = timezone.now().date()
    dates = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(6, -1, -1)]
    values = []
    
    for date in dates:   
        
        logs = RpaLogSuccess.objects.filter(start_time__date=date)
        total_duration = timedelta()

        for log in logs:
            if log.duration:
                total_duration+=log.duration    
        
        values.append(total_duration.total_seconds()/3600)
        
    return dict(
        dates=dates,
        values=values
    )

#Erros diários no últimos 7 dias
def get_erros_diarias():
    today = timezone.now().date()
    dates = [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(6, -1, -1)]
    values = []
    
    for date in dates:   
        
        total_erros = RpaLogError.objects.filter(start_time__date=date).count()
        
        values.append(total_erros)
        
    return dict(
        dates=dates,
        values=values
    )


def get_horas_mensais_by_rpa():
    
    
    rpas = Rpa.objects.all()
    
    tempo_por_mes = {rpa.name: {} for rpa in rpas}

    for rpa in rpas:
        tempos = RpaLogSuccess.objects.filter(rpa_id=rpa.id) \
            .annotate(
                year=ExtractYear('start_time'),
                month=ExtractMonth('start_time')
            ) \
            .values('year', 'month') \
            .annotate(total_duration=Sum('duration')) \
            .order_by('year', 'month')

        for tempo in tempos:
            month_str = f"{tempo['year']}-{tempo['month']:02d}"
            total_duration_seconds = tempo['total_duration'].total_seconds() if tempo['total_duration'] else 0
            tempo_por_mes[rpa.name][month_str] = total_duration_seconds

    meses = sorted({mes for mes_list in tempo_por_mes.values() for mes in mes_list})
    
    resultado = {
        rpa: [tempo_por_mes[rpa].get(mes, 0) for mes in meses] for rpa in tempo_por_mes
    }

    return {
        'meses': meses,
        'dados': resultado
    }

    

def get_erros_mensais_by_rpa():

    rpas = Rpa.objects.all()

    erros_por_mes = {rpa.name: {} for rpa in rpas}

 
    for rpa in rpas:
        erros = RpaLogError.objects.filter(rpa_id = rpa.id) \
        .annotate(
            year = ExtractYear('start_time'),
            month = ExtractMonth('start_time')
        )\
        .values('year','month')\
        .annotate(count=Count('id'))\
        .order_by('year','month')


        for erro in erros:
            month_str = f"{erro['year']}-{erro['month']:02d}"
            erros_por_mes[rpa.name][month_str] = erro['count']

    meses = sorted({mes for mes_list in erros_por_mes.values() for mes in mes_list})
    resultado = {
        rpa: [erros_por_mes[rpa].get(mes, 0) for mes in meses] for rpa in erros_por_mes
    }

    return {
        'meses': meses,
        'dados': resultado
    }


    





