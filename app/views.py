from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .paginations import *
from .serializers import *


# Create your views here.
@api_view(['GET'])
def index(request):
    p1={
        "tittle":"potato",
        "rate":"30 Tk",
        "is_available":"yes"
    }
    p2={
        "tittle":"apple",
        "rate":"200 Tk",
        "is_available":"no"
    }
    products=[p1,p2]
    return Response(products)

@api_view(['GET', 'POST'])
def todo_list(request):
    todos=Todo.objects.all()
    if request.method == 'GET':
        paginator=TodoPagination()
        page=paginator.paginate_queryset(todos, request)
        if page is not None:
            serializer=TodoListSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer=TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data=request.data
        serializer=TodoCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
@api_view(['GET','PATCH','DELETE'])
def todo_detail(request, id):
    todo=get_object_or_404(Todo, id=id)
    if request.method == 'GET':
        serializer=TodoDetailSerializer(todo)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        data=request.data
        serializer=TodoDetailSerializer(todo,data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        message=["Todo has benn deleted successfully"]
        return Response(message, status=status.HTTP_204_NO_CONTENT)