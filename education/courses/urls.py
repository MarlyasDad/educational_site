from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.AllCoursesListView.as_view(), name='all_courses'),
    path('category/<str:category>/', views.AllCoursesListView.as_view(), name='course_category'),
    path('detail_course/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('create_course/', views.CourseCreateView.as_view(), name='create_course'),
    path('update_course/<int:pk>/', views.CourseUpdateView.as_view(), name='update_course'),
    path('delete_course/<int:pk>/', views.CourseDeleteView.as_view(), name='delete_course'),
]
