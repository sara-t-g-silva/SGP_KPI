from api_client.authentication import Auth



def connection(username, password):
    auth_service = Auth()

    response = auth_service.get_token(
        username=username,
        password=password,
    )
    if response and response.get('error'):
        print(f'Falha ao realizar login: {response.get("error")}')
    else:
       token = response.get('access')
       print('Conexão na API realizada com sucesso!')

       return token
    
    
