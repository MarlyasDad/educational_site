from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView,\
    UpdateView, DeleteView, ListView
from .models import Course, Category


class AllCoursesListView(ListView):
    model = Course
    context_object_name = 'courses_list'
    paginate_by = 15
    template_name = 'courses/all_courses.html'

    def get_queryset(self):
        object_list = Course.objects.order_by('-start')
        search = self.request.GET.get('search')
        if search:
            object_list = object_list.filter(title__icontains=search)
        category_name = self.kwargs.get('category')
        if category_name:
            object_list = object_list.filter(category__name=category_name)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"search": self.request.GET.get('search')})
        raw_category = self.kwargs.get('category')
        if raw_category:
            category = Category.objects.get(name=raw_category)
            context.update({"category": category.alias})
        return context


class CourseCreateView(CreateView):

    model = Course
    fields = ['start', 'title', 'text', 'time_to_read', 'level', 'category']
    # fields = '__all__'
    # success_url = '/'

    def get_success_url(self):
        return '/detail_course/{}/'.format(self.object.pk)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    fields = ['start', 'title', 'text', 'time_to_read', 'level', 'category']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return '/detail_course/{}/'.format(self.object.pk)

    def get_object(self, queryset=None):
        obj = super(CourseUpdateView, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:all_courses')

    def get_object(self, queryset=None):
        obj = super(CourseDeleteView, self).get_object()
        if not obj.author == self.request.user:
            raise Http404
        return obj


class CourseDetailView(DetailView):

    model = Course
