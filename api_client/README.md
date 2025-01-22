## Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:
```bash
pip install -r requirements.txt
```
## Passo a passo para consumir a API no RPA

Com o acesso admin no django é necessário adicionar o RPA que deseja comece a ser monitorado. 

- 1. Adicionar o nome do RPA que deseja que seja monitorado pela API e salvar. 
> A primeiro momento as credenciais da api ficaram setadas no código.
- 2. Baixar dependências listadas no arquivo `requirements.txt` -> seguir o passo acima de instalação de dependências.
> Na pasta API terá a autenticação do para acessar a API e conexão que retorna o token para realizar os post no BD.
- 3. Importar a autenticação e conexão da API no rpa que deseja realizar os POSTs. Username e password seráo as credenciais para acessar a API. 
- 4. O token ficará salvo no código para ser utilizado nas requisições posts que serão feitas no código. 
```bash
from api.conection import conection
    token = conection('username','password')
```
- 5. Importar resquest.api, lá conterá os códigos para realizar post na API. 
```bash
from api.resquest_api import post_log_rpa_error, post_log_rpa_success,put_status_rpa
    post_log_rpa_success(token=token,id=rpa_id,tempo_inicial=tempo_inicial,tempo_final=tempo_final,message=message)

    post_log_rpa_error(token=token,id=rpa_id,tempo_inicial=tempo_inicial,tempo_final=tempo_final,message=message)
```
## Rodar o projeto

Após instalar as dependências, execute o projeto com:
```bash
python3 manage.py runserver
```

## Deixando API disponível em rede utilizando o NGROK:

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Ngrok disponível para download em: [Ngrok](https://dashboard.ngrok.com/get-started/setup/linux)

# Colocando aplicação online: 

```bash h
ngrok http --domain=welcome-thoroughly-whale.ngrok-free.app 8000
```


Após isso, o sistema estará pronto para ser acessado em:
[RPA_KPI](https://welcome-thoroughly-whale.ngrok-free.app)

**IMPORTANTE!** 
No ngrok conta free somente é possível criar três túneis, dessa forma somente é possível deixar uma aplicação online por conta. Seja o streamlit ou a API. 