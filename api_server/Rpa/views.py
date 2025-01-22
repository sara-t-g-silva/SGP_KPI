from django.db.models import (
    Count,
    Sum,
    Max)
from rest_framework import (
    generics,
    views,
    status,
    response)
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, 
    IsAuthenticated)
from Rpa.models import (
    Rpa_model,
    Log_rpa_model, 
    Log_rpa_error_model)
from Rpa.serializers import (
    RpaSerializer, 
    Log_rpaSerializer,
    Log_rpa_error_model_serializer)
#permissoes não globais
'''from Rpa.permissions import (
    Rpa_model_permissions_class,
    Log_rpa_model_permissions_class,
    Log_rpa_error_model_permissions_class)'''
#permissoes globais incluidas diretamente no app
from app.permissions import GlobalDefaultPermissions




#migrando para utilizar django rest framework

class RpaCreateListView(generics.ListCreateAPIView):
    #PROTEGENDO O ENDPOINT PARA REALIZAR AUTENTICAÇÃO 
    permission_classes = (IsAuthenticated,GlobalDefaultPermissions)
    queryset = Rpa_model.objects.all()
    serializer_class = RpaSerializer


class RpaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissions)
    queryset = Rpa_model.objects.all()
    serializer_class = RpaSerializer


class LogRpaCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissions)
    queryset = Log_rpa_model.objects.all()
    serializer_class = Log_rpaSerializer

    
class LogRpaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissions)
    queryset = Log_rpa_model.objects.all()
    serializer_class = Log_rpaSerializer

class Log_rpa_error_model_CreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissions)
    queryset = Log_rpa_error_model.objects.all()
    serializer_class = Log_rpa_error_model_serializer

    
class Log_rpa_error_model_RetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissions)
    queryset = Log_rpa_error_model.objects.all()
    serializer_class = Log_rpa_error_model_serializer


#métodos distintos para retornar estatísitica específicas.
class RpaStaticsView(views.APIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermissions)
    queryset = Rpa_model.objects.all()
    #name,status,tempo total, quantidade de erros.

    
    def get(self,request):
        #capitaurar dados
        #monta os dados
        #retorna a visualização
        id_especificos = [4,50,77,78]
        #retorna nomes de rpas específicos de acordo com o id presente no array id_especifico
        names = self.queryset.filter(id__in=id_especificos).values('name')
        #quantidade de erros 
        #status_Rpa = self.queryset.filter(id__in=id_especificos).values('rpa_status').annotate(count=Count('rpa_status'))
        rpas = self.queryset.filter(id__in=id_especificos).values('name').annotate(
            tempo_total=Sum('duration'),
            quantidade_erros=Sum('error_count'),
            status_rpa=Max('rpa_status')
        )
        tempo_total = self.queryset.filter(id__in=id_especificos).values('name').annotate(tempo_total=Sum('duration'))
        quantidade_erros = self.queryset.filter(id__in=id_especificos).values('name').annotate(quantidade_erros=Sum('error_count'))
        #traz o status do rpa de acordo com o nome
        status_rpa = self.queryset.filter(id__in=id_especificos).values('name').annotate(status_rpa=Max('rpa_status'))
    
            

        return response.Response(
            
            data={
                    "names" : names,
                    "rpas":rpas,
                    "tempo_total":tempo_total,
                    "quantidade_de_erros":quantidade_erros,
                    "status_rpa":status_rpa
                    
                
                 },
            status = status.HTTP_200_OK
            
        )
        
        '''"status_Rpa": status_Rpa,
                    "Tempo_total": tempo_total,
                    "quantidade_erros":quantidade_erros,
                    "status_rpa":status_rpa'''









    

#SEGURANÇA DA REQUISIÇÃO POST
#REQUISIÇÕES SEM FRAMEWORK
'''@csrf_exempt
def rpa_view(request):
    #data = [{'id':rpas.id,'name':rpas.name,'status':rpas.status,'description':rpas.description,'version':rpas.version} for rpa in rpas]
    
    if request.method == 'GET':
        #Lista todos os elementos
        rpas = Rpa.objects.all()
        data = []
        for rpa in rpas:
            rpa_data = {
                'id': rpa.id,
                'name': rpa.name,
                'rpa_status': rpa.rpa_status,
                'description': rpa.description,
                'version': rpa.version
            }
            #adiciona dentro do rpa_data
            data.append(rpa_data)

        return JsonResponse(data, safe=False)
    #slva elementos na tabela RPA
    if request.method ==  'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_rpa = Rpa(
            name=data['name'],
            rpa_status=data['rpa_status'],
            description=data['description'],
            version=data['version'])

        new_rpa.save()
    #return será o que será salvo no new_rpa
        return JsonResponse(
            {
                'id': new_rpa.id,
                'name': new_rpa.name,
                'rpa_status': new_rpa.rpa_status,
                'description': new_rpa.description,
                'version': new_rpa.version
                }, 
                
                status= 201
                )'''
'''@csrf_exempt
def rpa_view_details(request, pk):
     #Django já fornece a opção de tratativa de não encontrar o id
    rpa = get_object_or_404(Rpa, pk = pk)
    #rpa = Rpa.objects.get(pk=pk)
    if request.method == 'GET':
       
        data = {
                'id': rpa.id,
                'name': rpa.name,
                'rpa_status': rpa.rpa_status,
                'description': rpa.description,
                'version': rpa.version
                } 
        return JsonResponse(data)
    #atualizado dados do usuário
    if request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))

        rpa.name = data['name'],
        rpa.rpa_status = data['rpa_status'],
        rpa.description = data['description'],
        rpa.version = data['version']

        rpa.save()
        return JsonResponse(
                {   
                    'id': rpa.id,
                    'name': rpa.name,
                    'rpa_status': rpa.rpa_status,
                    'description': rpa.description,
                    'version': rpa.version
                }, 
                
                status= 203
                )
    if request.method == 'DELETE':
        rpa.delete()
        return JsonResponse(
            {'Message':'Rpa excluído com sucesso!'},
            status = 204
        )
'''

    

    


