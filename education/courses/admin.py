from django.contrib import admin

from .models import Course, Category, Lesson, Schedule


# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = 'id', 'first_name', 'last_name', 'full_name'
#     list_display_links = 'id', 'full_name'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'author'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = 'id', 'start'
