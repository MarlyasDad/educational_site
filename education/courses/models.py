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
    LEVEL_OF_COMPLEXITY = (
        (1, 'EASY'),
        (2, 'MEDIUM'),
        (3, 'HARD'),
        (4, 'IMPOSSIBLE'),
    )

    AVERAGE_DURATION = (
        (1, '<= 1 day'),
        (2, '<= 1 week'),
        (3, '<= 1 month'),
        (4, '<= 6 month'),
        (5, '<= 1 year'),
    )

    title = models.CharField(max_length=254)
    text = models.TextField()
    time_to_read = models.IntegerField(choices=AVERAGE_DURATION)
    level = models.IntegerField(choices=LEVEL_OF_COMPLEXITY, default=2)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)


class Lesson(models.Model):

    title = models.CharField(max_length=254, default='Unnamed lesson')
    description = models.CharField(max_length=254, blank=True)
    text = models.TextField(blank=True)
    video = models.CharField(max_length=254, null=True)  # Path to video file
    stream_url = models.CharField(max_length=254, null=True)  # Stream url (like zoom)
    materials = models.CharField(max_length=254, null=True)  # Link to materials repository
    course = models.ForeignKey(Course, on_delete=models.PROTECT, null=True)
    is_live = models.BooleanField(default=False)  # 1 - is live, 0 - is recorded


class Schedule(models.Model):
    start = models.DateTimeField()
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, null=True)
    is_cancelled = models.BooleanField(default=False)
