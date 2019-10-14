from django.urls import path , re_path
from .views import classes_views

urlpatterns = [
    path('classes', classes_views.AllClassesController.as_view()),    
    path('class/<int:class_id>/students', classes_views.ClassStudentsController.as_view()),
    path('class/<int:class_id>/performance', classes_views.ClassPerformanceController.as_view()),
    path('class/<int:class_id>/student/<int:student_id>', classes_views.DetailedScoresController.as_view()),
]
