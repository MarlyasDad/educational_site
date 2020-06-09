from django.core import mail
from django_rq import job

from authapp.models import CourseUser


@job
def send_mail_to_admin():
    subject = 'GamesEdu admin notification'
    body = 'You received a new message from the feedback form.'
    from_ = 'notify@gamesedu.com'
    to = ['admin@gamesedu.com', ]
    with mail.get_connection() as connection:
        mail.EmailMessage(
            subject, body, from_, to,
            connection=connection,
        ).send()


@job
def send_mail_to_user(email: str):
    subject = 'GamesEdu user notification'
    body = 'Your message has been saved and will soon be viewed' \
           'by the administrator.'
    from_ = 'notify@gamesedu.com'
    to = [email, ]
    with mail.get_connection() as connection:
        mail.EmailMessage(
            subject, body, from_, to,
            connection=connection,
        ).send()
