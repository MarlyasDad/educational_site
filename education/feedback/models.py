from django.utils import timezone
from django.db import models
from courses.models import CourseUser


class Feedback(models.Model):
    create = models.DateTimeField('Дата создания', null=True, default=timezone.now())
    title = models.CharField('Заголовок', max_length=254)
    text = models.TextField('Что Вы хотите написать', blank=True)
    author = models.ForeignKey(CourseUser, on_delete=models.PROTECT, null=False)
