from django.urls import path , re_path
from .views import student_views

urlpatterns = [
    path('', student_views.DbController.as_view()),    
    path('students', student_views.AllStudentsController.as_view()),
    path('student/<int:student_id>/classes', student_views.StudentsClassesController.as_view()),
    path('student/<int:student_id>/performance', student_views.StudentsPerformanceController.as_view()),
    path('student/<int:student_id>/class/<int:class_id>', student_views.DetailedScoresController.as_view()),
]
