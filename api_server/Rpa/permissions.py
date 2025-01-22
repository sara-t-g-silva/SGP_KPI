
#Class de exemplo para criação de permissons

from rest_framework import permissions

class Rpa_model_permissions_class(permissions.BasePermission):

    def has_permission(self, request, view):
        # se o usuário fizer um get, retorna a views do rpa, métodos seguros
        if request.method in ['GET', 'OPTIONS','HEAD']:
            return request.user.has_perm('Rpa.view_rpa_model') #Nome do app, método e nome do model, o nome do model pode ser usado maisculo ou minusculo
        
        if request.method == 'POST':
            #se o usuário estiver configurado no servidor django para add, dessa forma entendesse que o mesmo pode incluir dados.
            return request.user.has_perm('Rpa.add_rpa_model')

        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('Rpa.change_rpa_model')
        
        if request.method == 'DELETE':
            return request.user.has_perm('Rpa.delete_rpa_model')
        
        return False
        

class Log_rpa_model_permissions_class(permissions.BasePermission):
        
    def has_permission(self, request, view):

        
        if request.method in ['GET', 'OPTIONS','HEAD']:
                return request.user.has_perm('Rpa.view_log_rpa_model') #Nome do app, método e nome do model, o nome do model pode ser usado maisculo ou minusculo
            
        if request.method == 'POST':
                #se o usuário estiver configurado no servidor django para add, dessa forma entendesse que o mesmo pode incluir dados.
                return request.user.has_perm('Rpa.add_log_rpa_model')

        if request.method in ['PUT', 'PATCH']:
                return request.user.has_perm('Rpa.change_log_rpa_model')
            
        if request.method == 'DELETE':
                return request.user.has_perm('Rpa.delete_log_rpa_model')
            
        return False
            
class Log_rpa_error_model_permissions_class(permissions.BasePermission):
        
        def has_permission(self, request, view):
            
        
            if request.method in ['GET', 'OPTIONS','HEAD']:
                return request.user.has_perm('Rpa.view_log_rpa_error_model') #Nome do app, método e nome do model, o nome do model pode ser usado maisculo ou minusculo
            
            if request.method == 'POST':
                #se o usuário estiver configurado no servidor django para add, dessa forma entendesse que o mesmo pode incluir dados.
                return request.user.has_perm('Rpa.add_log_rpa_error_model')

            if request.method in ['PUT', 'PATCH']:
                return request.user.has_perm('Rpa.change_log_rpa_error_model')
            
            if request.method == 'DELETE':
                return request.user.has_perm('Rpa.delete_log_rpa_error_model')
            
            return False