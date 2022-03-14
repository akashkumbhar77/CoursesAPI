from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import  CoursesSerializers , ProductSerializer
from django.core.exceptions import ObjectDoesNotExist
from . import models

# Create your views here.

@api_view(["GET","POST"])
def getallData(request):
    if(request.method == 'GET'):
        data = models.CoursesModel.objects.all()
        serializer = CoursesSerializers(data , many=True)
    if(request.method == 'POST'):
        serializer = CoursesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def getCourseInfo(request,pk):
    try:
        course = models.CoursesModel.objects.get(pk=pk)
    except  ObjectDoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        course = models.CoursesModel.objects.get(pk=pk)
        serializer = CoursesSerializers(course)
        return Response(serializer.data)
    elif request.method == 'PUT':
        course = models.CoursesModel.objects.get(pk=pk)
        serializer = CoursesSerializers(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)

    elif request.method == 'DELETE':
        course.delete()
        return HttpResponse(status=204)


@api_view(['GET','POST'])
def getallProducts(request):
    if request.method == 'GET':
        data = models.Product.objects.all()
        serializer = ProductSerializer(data,many= True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer_post = ProductSerializer(data=request.data)
        if serializer_post.is_valid():
            serializer_post.save()
            return Response(serializer_post.data)
        else:
            return Response(serializer_post.errors)



@api_view(['GET','PUT','DELETE'])
def getProduct(request,pk):
    if request.method == 'GET':
        try:
            prod_data = models.Product.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'Error':'Product Doesnt exist'},status=status.HTTP_400_BAD_REQUEST)
        serialiser = ProductSerializer(prod_data)
        return Response(serialiser.data)

    elif request.method == 'PUT':
        prod_data = models.Product.objects.get(pk=pk)
        serializer = ProductSerializer(prod_data,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'DELETE':
        product = models.Product.objects.get(pk=pk)
        product.delete()
        return HttpResponse(status=204)


