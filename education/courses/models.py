from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = 'Categories'


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

    title = models.CharField(max_length=254)
    text = models.TextField()
    time_to_read = models.PositiveSmallIntegerField(choices=AVERAGE_DURATION, default=LEVEL_MEDIUM)
    level = models.PositiveSmallIntegerField(choices=LEVEL_OF_COMPLEXITY, default=DURATION_MONTH)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


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
    start = models.DateTimeField()
    lesson = models.OneToOneField(Lesson, on_delete=models.PROTECT, null=False)
    is_cancelled = models.BooleanField(default=False)
