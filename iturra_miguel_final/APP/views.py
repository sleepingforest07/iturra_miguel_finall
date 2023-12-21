from django.shortcuts import render,redirect
from .forms import FormInscritos, FormInstitucion
from .models import Instituciones, Inscritos
from .serializers import InscritoSerializer, InstitucionSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

def index(request):
    return render (request, 'TEMPLATESAPP/index.html')

def datosAutor(request):
    aut = {
        'nombre' : 'Miguel Iturra',
        'edad': 20,
        'email': 'MiguelIturra06@inacap.cl',
        'carrera': 'Ingeniería en Informática'
    }
    return JsonResponse(aut)


def agregar_institucion(request):
    form = FormInstitucion()
    if (request.method == 'POST'):
        form = FormInstitucion(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect ('index')
        
    data = {'form' : form}
    return render (request,'TEMPLATESAPP/formulario_institucion.html',data)

def agregar_participante(request):
    form = FormInscritos()
    if (request.method == 'POST'):
        form = FormInscritos(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect ('index')
        
    data = {'form' : form}
    return render (request,'TEMPLATESAPP/formulario_participante.html',data)


#class based views
class InscritosList(APIView):
    def get(self,request):
        inscri = Inscritos.objects.all()
        serial = InscritoSerializer(inscri, many=True)
        return Response(serial.data)
    
    def post(self,request):
        serial = InscritoSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    


class InscritosDetalle(APIView):
    def get_object(self,id):
        try:
            return Inscritos.objects.get(pk=id)
        except Inscritos.DoesNotExist:
            return Http404
        
    def get(self,request,id):
        Inscri = self.get_object(id)
        serial = InscritoSerializer(Inscri)
        return Response(serial.data)
    
    def put(self,request,id):
        Inscri = self.get_object(id)
        serial = InscritoSerializer(Inscri,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,id):
        Inscri = self.get_object(id)
        Inscri.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET','POST'])
def instituciones_list(request):
    if request.method == 'GET':
        insti = Instituciones.objects.all()
        seria = InstitucionSerializer(insti, many=True)
        return Response (seria.data)
    
    if request.method == 'POST':
        seria = InstitucionSerializer(data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data, status=status.HTTP_201_CREATED)
        
        return Response(seria.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def instituciones_detalle(request,id):
    try:
        insti = Instituciones.objects.get(pk=id)

    except Instituciones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerializer(insti)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = InstitucionSerializer(insti, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        insti.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
