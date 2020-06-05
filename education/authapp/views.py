from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import CourseUser
from .forms import CourseUserCreationForm


class LoginView(View):

    form = AuthenticationForm

    def get(self, request):
        form = self.form()
        return render(request, 'authapp/login.html', context={"form": form})

    def post(self, request):
        form = self.form(data=request.POST or None)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('courses:all_courses'))
        return render(request, 'authapp/login.html', context={"form": form})


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('courses:all_courses'))


class RegisterView(View):

    form = AuthenticationForm

    def get(self, request):
        form = CourseUserCreationForm()
        return render(request, 'authapp/register.html', context={"form": form})

    def post(self, request):
        form = CourseUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
        return render(request, 'authapp/register.html', context={"form": form})


class UserDetailView(DetailView):

    template_name = 'authapp/info.html'
    context_object_name = 'user'
    # model = CourseUser

    def get_object(self, queryset=None):
        obj = get_object_or_404(CourseUser, pk=self.request.user.pk)
        return obj
