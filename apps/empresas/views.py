from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from apps.empresas.models import Empresa
from apps.empresas.serializers import EmpresaSerializer


class JSONResponse(HttpResponse):
 
    # Redenriza elemento HttpResponse para JSON
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def empresa_lista(request):
    
    # Lista todas Empresas 
    if request.method == 'GET':
        empresa = Empresa.objects.all()
        serializer = EmpresaSerializer(empresa, many=True)
        return JSONResponse(serializer.data)
    
    # Adiciona uma nova Empresa
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmpresaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)