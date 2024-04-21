from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
# Importar as models (tabelas)
from .models import User
# Importar configurações para Json e HTTP
from django.http import JsonResponse
import json
# Buscar o token
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):

    # Verificamos se o método da solicitação é POST
    if request.method == 'POST':

        # Obter o corpo da solicitação e carregar os dados JSON
        data = json.loads(request.body)

        # Verificar se os campos de email e senha estão presentes
        email = data.get('email')
        password = data.get('password')

        # Se ambos os campos estiverem presentes, continue com o processamento
        if email and password:
            
            # Sua lógica de criação de usuário aqui
            return JsonResponse({'message': 'Cadastro realizado com sucesso'})
        
        else:

            errors = {
                'email': [{'message': 'Este campo é obrigatório.', 'code': 'required'}] if not email else [],
                'password': [{'message': 'Este campo é obrigatório.', 'code': 'required'}] if not password else [],
            }

            return JsonResponse({'errors': errors}, status=400)
        
    else:

        return JsonResponse({'error': 'Método não permitido'}, status=405)
    
@csrf_exempt
def login(request):

    # Verificamos se o método da solicitação é POST
    if request.method == 'POST':

        # Obter o corpo da solicitação e carregar os dados JSON
        data = json.loads(request.body)

        # Verificar se os campos de email e senha estão presentes
        email = data.get('email')
        password = data.get('password')

        if email and password:

            try:

                # Buscar o usuário no banco de dados pelo email
                user = User.objects.get(email=email)

                if password == user.password:

                    # Definir a duração da sessão
                    request.session.set_expiry(86400)

                    # Armazenar o ID do usuário na sessão
                    request.session['user_id'] = user.id

                    # Retornar uma mensagem de sucesso
                    return JsonResponse({'message': 'Login realizado com sucesso', 'id': user.id})
                
                else:

                    # Senha incorreta, retornar mensagem de erro
                    return JsonResponse({'error': 'Credenciais inválidas'}, status=400)
                
            except User.DoesNotExist:

                # Usuário não encontrado, retornar mensagem de erro
                return JsonResponse({'error': 'Usuário não encontrado'}, status=404)
            
        else:
            
            errors = {
                'email': [{'message': 'Este campo é obrigatório.', 'code': 'required'}] if not email else [],
                'password': [{'message': 'Este campo é obrigatório.', 'code': 'required'}] if not password else [],
            }

            return JsonResponse({'errors': errors}, status=400)
        
    else:
        
        # Método não permitido, retornar mensagem de erro
        return JsonResponse({'error': 'Método não permitido'}, status=405)