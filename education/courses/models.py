from django.db import models
from authapp.models import CourseUser


class Category(models.Model):
    name = models.CharField(max_length=254, unique=True)
    alias = models.CharField(max_length=254, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Category: {self.name}>'


class Course(models.Model):
    LEVEL_EASY = 1
    LEVEL_MEDIUM = 2
    LEVEL_HARD = 3
    LEVEL_OF_COMPLEXITY = (
        (LEVEL_EASY, 'EASY'),
        (LEVEL_MEDIUM, 'MEDIUM'),
        (LEVEL_HARD, 'HARD'),
    )
    DURATION_DAY = 1
    DURATION_WEEK = 2
    DURATION_MONTH = 3
    DURATION_HALF_YEAR = 4
    DURATION_YEAR = 5

    AVERAGE_DURATION = (
        (DURATION_DAY, '<= 1 day'),
        (DURATION_WEEK, '<= 1 week'),
        (DURATION_MONTH, '<= 1 month'),
        (DURATION_HALF_YEAR, '<= 6 month'),
        (DURATION_YEAR, '<= 1 year'),
    )

    start = models.DateField(null=True)
    title = models.CharField(max_length=254)
    text = models.TextField()
    time_to_read = models.PositiveSmallIntegerField(choices=AVERAGE_DURATION, default=DURATION_MONTH)
    level = models.PositiveSmallIntegerField(choices=LEVEL_OF_COMPLEXITY, default=LEVEL_MEDIUM)
    author = models.ForeignKey(CourseUser, on_delete=models.PROTECT, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'<Course: {self.title} {self.author} {self.category.name} {self.time_to_read}>'


class Lesson(models.Model):
    title = models.CharField(max_length=254, default='Unnamed lesson')
    description = models.CharField(max_length=254, blank=True)
    text = models.TextField(blank=True)
    video = models.FileField(null=True)  # Path to video file
    stream_url = models.URLField(null=True)
    materials = models.URLField(null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    is_live = models.BooleanField(default=False)


class Schedule(models.Model):
    start = models.DateTimeField(null=True)
    lesson = models.OneToOneField(Lesson, on_delete=models.PROTECT, null=False)
    is_cancelled = models.BooleanField(default=False)
