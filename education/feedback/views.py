from datetime import datetime
from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from .models import Feedback
from .forms import FeedbackForm
from . import tasks


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm

    def get_success_url(self):
        return reverse('feedback:create_success')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.create = datetime.now()
        admin_job = tasks.send_mail_to_admin.delay()
        user_job = tasks.send_mail_to_user.delay(self.request.user.email)
        return super(FeedbackCreateView, self).form_valid(form)


class SuccessTemplateView(TemplateView):
    template_name = 'feedback/feedback_success.html'