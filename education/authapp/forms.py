from django.contrib.auth.forms import UserCreationForm

from .models import CourseUser


class CourseUserCreationForm(UserCreationForm):
    class Meta:
        model = CourseUser
        fields = ('username', 'email', 'password1', 'password2',)
