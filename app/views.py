from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
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

@api_view(['GET'])
def todo_list(request):
    todos=Todo.objects.all()
    paginator=TodoPagination()
    page=paginator.paginate_queryset(todos, request)
    if page is not None:
        serializer=TodoListSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    serializer=TodoListSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todo_detail(request, id):
    todo=get_object_or_404(Todo, id=id)
    serializer=TodoDetailSerializer(todo)
    return Response(serializer.data)