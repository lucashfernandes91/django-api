from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from apps.funcionarios.models import Funcionario
from apps.funcionarios.serializers import FuncionarioSerializer


class JSONResponse(HttpResponse):

    # Redenriza elemento HttpResponse para JSON
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def funcionario_lista(request):

    # Lista todos Funcionari@s 
    if request.method == 'GET':
        funcionario = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionario, many=True)
        return JSONResponse(serializer.data)

    # Cria um@ nov@ funcionari@
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FuncionarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def funcionario_detalhes(request, username):

    # Verificar se funcionari@ existe no banco de dados
    try:
        funcionario = Funcionario.objects.get(username=username)
    except Funcionario.DoesNotExist:
        return HttpResponse(status=404)

    # Lista Funcionário
    if request.method == 'GET':
        serializer = FuncionarioSerializer(funcionario)
        return JSONResponse(serializer.data)

    # Atualiza dados do Funcionario
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FuncionarioSerializer(funcionario, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    # Deleta Funcionári@
    elif request.method == 'DELETE':
        funcionario.delete()
        return HttpResponse(status=204)