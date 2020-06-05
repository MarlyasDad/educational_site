from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models


class SendEmailMixin:
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class CourseUser(AbstractUser, SendEmailMixin):
    MALE = 'm'
    FEMALE = 'f'
    SEX_CHOICES = (
        (MALE, 'Мужской'),
        (FEMALE, 'Женский')
    )

    birth_date = models.DateField('Дата рождения', null=True)
    city = models.CharField('Город', max_length=127, blank=True)
    sex = models.CharField('Пол', max_length=1, choices=SEX_CHOICES,
                           default=SEX_CHOICES[0][0])

    # def __str__(self):
    #     return f'{self.first_name} {self.last_name} ({self.username}), ' \
    #            f'{self.email}, {self.city}, {self.get_sex_display()}, ' \
    #            f'{self.birth_date}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name
