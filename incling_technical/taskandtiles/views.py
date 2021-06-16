from django.shortcuts import render
from .models import Task,Tile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer,TileSerializer

@api_view(['GET'])
def home(request):
    api_urls = {
        'Tasks List':'/task-list/',
        'Tasks Add':'/task-create/',
        'Tasks update':'/task-update/<str:pk>/',
        'Tasks delete':'/task-delete/<str:pk>/',
        'Tile List': '/tile-list/',
        'Tile Add': '/tile-create/',
        'Tile update': '/tile-update/<str:pk>/',
        'Tile delete': '/tile-delete/<str:pk>/'

    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data = request.data)
    print(serializer)
    if serializer.is_valid():
        print("saved!")
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance = tasks ,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    tasks = Task.objects.get(id = pk)
    tasks.delete()
    return Response("Contact Deleted")

@api_view(['GET'])
def tileList(request):
    tile = Tile.objects.all()
    serializer = TileSerializer(tile, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def tileCreate(request):
    serializer = TileSerializer(data = request.data)
    print(serializer)
    if serializer.is_valid():
        print("saved!")
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def tileUpdate(request, pk):
    tile = Tile.objects.get(id = pk)
    serializer = TileSerializer(instance = tile ,data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def tileDelete(request,pk):
    tile = Tile.objects.get(id = pk)
    tile.delete()
    return Response("Contact Deleted")
