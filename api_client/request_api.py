import requests
import time


def post_log_rpa_sucess(token,id,tempo_inicial,tempo_final,message):
    
    base_url = 'https://welcome-thoroughly-whale.ngrok-free.app/api/v1/'
    rpas_url_log = f'{base_url}rpa_success/'
    headers = {'Authorization': f'Bearer {token}'}

    start_time_str = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(tempo_inicial))
    end_time_str = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(tempo_final))
    duration = int(tempo_final - tempo_inicial)

    print(duration)

    # Formatando a duração em horas, minutos e segundos
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    duration_formatted = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
     
    dados = {
    "rpa_id": id,
    "start_time": start_time_str,
    "end_time": end_time_str,
    "duration": duration_formatted,
    "rpa_log_status": "success",
    "message": message
    }

    response = requests.post(rpas_url_log,headers=headers,json=dados)
    

    if response.status_code == 201:
        response = response.json()
        print(f'Log salvo com sucesso através API local', response)
    else:
        print(f'Falha na requisição POST a API: {response.status_code}')
        print('Detalhes: ', response.text)


def post_log_rpa_error(token,id,tempo_inicial,tempo_final,message):

    base_url = 'https://welcome-thoroughly-whale.ngrok-free.app/api/v1/'
    rpas_url_error_log = f'{base_url}rpa_error/'
    headers = {'Authorization': f'Bearer {token}'}

    start_time_str = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(tempo_inicial))
    end_time_str = time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(tempo_final))
    duration = int(tempo_final - tempo_inicial)

    # Formatando a duração em horas, minutos e segundos
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = duration % 60
    duration_formatted = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
     
    dados = {
    "rpa_id": id,
    "start_time": start_time_str,
    "end_time": end_time_str,
    "duration": duration_formatted,
    "rpa_log_status": "fault",
    "message": message
    }

    response = requests.post(rpas_url_error_log,headers=headers,json=dados)
    

    if response.status_code == 201:
        response = response.json()
        print(f'Log salvo com sucesso através API local', response)
    else:
        print(f'Falha na requisição POST a API: {response.status_code}')
        print('Detalhes: ', response.text)


def put_status_rpa(token,id,status):

    base_url = 'https://welcome-thoroughly-whale.ngrok-free.app/api/v1/rpas/'
    rpas_url_put = f'{base_url}{id}/'
    headers = {'Authorization': f'Bearer {token}'}
   
    
    

    dados = {
        "rpa_status": status,
       }

    response = requests.put(rpas_url_put,headers=headers,json=dados)   

    if response.status_code == 200:
        response = response.json()
        
        print('Status RPA - atualizado com sucesso')
        print(status)
    else: 
        print(f'Falha na requisição PUT a API: {response.status_code}')
        print('Detalhes: ', response.text)