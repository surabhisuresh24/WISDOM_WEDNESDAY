# wwq/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/', views.user_details, name='details'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('department/<str:dept_name>/', views.department_page, name='department_page'),
    path('it_policies/', views.it_policies, name='it_policies'),
    path('hr_policies/', views.hr_policies, name='hr_policies'),
    path('courses/', views.courses, name='courses'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz_result/<int:score>/', views.quiz_result, name='quiz_result'),
]
