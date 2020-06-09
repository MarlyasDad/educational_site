from django.core.management import BaseCommand
from mixer.backend.django import mixer
# from authapp.models import BlogUser
from courses.models import Category, Course, Lesson, Schedule
from authapp.models import CourseUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        # pass
        # categories = mixer.cycle(4).blend(
        #     Category,
        #     name=mixer.sequence('Card', 'PC', 'Console', 'Board')
        # )
        #
        # for category in categories:
        #     category.save()

        users = mixer.cycle(10).blend(CourseUser)
        for user in users:
            user.save()

        courses = mixer.cycle(15).blend(
            Course,
            author=mixer.SELECT,
            category=mixer.SELECT,
            time_to_read=mixer.RANDOM,
        )
        for course in courses:
            course.save()

        lessons = mixer.cycle(45).blend(
            Lesson,
            course=mixer.SELECT,
        )
        for lesson in lessons:
            lesson.save()

        schedule = mixer.cycle(len(lessons)).blend(
            Schedule,
            lesson=(a for a in lessons),
        )

        for s in schedule:
            s.save()
