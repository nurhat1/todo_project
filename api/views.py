from functools import partial
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import TaskListSerializer, TaskDetailSerializer
from .services import get_list_of_tasks, get_task_by_id
from .models import Task

# Create your views here.


@api_view(['GET', 'POST'])
def task_list(request):
    """
    Return list of all tasks or create a new task
    """

    # create a new task
    if request.method == 'POST':
        task_serializer = TaskDetailSerializer(data=request.data)
        if task_serializer.is_valid():
            task_serializer.save()
        else:
            return Response({
                "message": "Fields are incorrectly filled", 
                "status": status.HTTP_400_BAD_REQUEST
            })

    tasks = get_list_of_tasks()
    tasks_serializer = TaskListSerializer(tasks, many=True)

    return Response({
        "message": "success", 
        "data": tasks_serializer.data, 
        "status": status.HTTP_200_OK
    })


@api_view(['GET', 'PATCH', 'DELETE'])
def task_detail(request, pk):
    """
    Get, edit or delete task by id
    """

    try:
        # get task by id
        task = get_task_by_id(pk)

        # edit the task
        if request.method == 'PATCH':
            task_serializer = TaskDetailSerializer(instance=task, data=request.data, partial=True)
            if task_serializer.is_valid():
                task_serializer.save()
                return Response({
                    "message": "Task updated successfully", 
                    "data": task_serializer.data, 
                    "status": status.HTTP_200_OK
                })
            else:
                return Response({
                    "message": "Fields are incorrectly filled", 
                    "status": status.HTTP_400_BAD_REQUEST
                })

        # delete the task
        if request.method == 'DELETE':
            task.delete()
            return Response({
                "message": "Task deleted successfully", 
                "status": status.HTTP_200_OK
            })

        task_serializer = TaskDetailSerializer(task)
        return Response({
            "message": "success", 
            "data": task_serializer.data, 
            "status": status.HTTP_200_OK
        })
    except Task.DoesNotExist:
        return Response({
            "message": f"Task with id {pk} does not exist", 
            "status": status.HTTP_404_NOT_FOUND
        })
    except Exception:
        return Response({
            "message": "An error occurred on the server side, please try again later",
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR
        })
