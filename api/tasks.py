from django.core.mail import EmailMessage

from todo_project.celery import app


@app.task
def send_email_task(text: str, recipient: str) -> None:
    """
    Celery task that send email to the recipient with given text

    :param text: text of the email message
    :type text: str
    :param recipient: recipient email
    :type recipient: str
    """
    try:
        # send email
        email_ = EmailMessage(
            'Notification from TodoProject',
            f'{text}',
            'noreply@gmail.com',
            [recipient],
        )
        email_.send(fail_silently=False)
    except Exception as e:
        print("Exception in send_email_task(): ", e)
