from typing import List

from django.core.mail import EmailMessage

from .models import Task
from .tasks import send_email_task


def get_list_of_tasks() -> List[Task]:
    """
    Return list of all tasks

    :return tasks: list of all Task objects
    :rtype: list
    """
    tasks = Task.objects.all()
    return list(tasks)


def get_task_by_id(pk: int) -> Task:
    """
    Return Task object by id or raise exceptions

    :param pk: id of Task object
    :type pk: int

    :return task: Task object
    :rtype: Task
    """
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist as e:
        print(f"Task object with id {pk} does not exist")
        raise
    except Exception as e:
        print(f"An exception {e} was thrown")
        raise

    return task


def execute_task(task: Task) -> None:
    """
    Execute task by set 'is_executed' to True. If it is already True, change to False.
    Send email to the user about task execution.

    :param task: Task object
    :type task: Task
    """
    if task.is_executed:
        task.is_executed = False
        send_email_task.delay(f"Task <{task.title}> is unmarked.", "ibragimnurhat@gmail.com")
    else:
        task.is_executed = True
        send_email_task.delay(f"Task <{task.title}> is executed.", "ibragimnurhat@gmail.com")
    task.save()
