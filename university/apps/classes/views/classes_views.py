from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status
from ..services.classes_service import ClassesService
from apps.students.services.student_service import StudentsService
import logging
import time
from bson.json_util import dumps
import traceback
# Create your views here.

class AllClassesController(views.APIView):

    log = logging.getLogger(__name__)
    classes_object = ClassesService()
    def get(self, request):
        start_get = time.time()
        print("started")
        try:
            data = self.classes_object.fetch_all_classes()
            print("abc")
            return Response(data, status=status.HTTP_200_OK, headers=None)
        # Handling excepitons
        except Exception as e:
            print(traceback.format_exc())
        
        finally:
            self.log.info("END : {0}".format(time.time()))
            self.log.info("Total execution time : {0}".format(time.time()-start_get))

class ClassStudentsController(views.APIView):

    log = logging.getLogger(__name__)
    classes_object = ClassesService()
    def get(self, request,class_id):
        start_get = time.time()
        print("started")
        try:
            data = self.classes_object.fetch_students_of_class(class_id)
            print("abc")
            return Response(data, status=status.HTTP_200_OK, headers=None)
        # Handling excepitons
        except Exception as e:
            print(traceback.format_exc())
        
        finally:
            self.log.info("END : {0}".format(time.time()))
            self.log.info("Total execution time : {0}".format(time.time()-start_get))

class ClassPerformanceController(views.APIView):

    log = logging.getLogger(__name__)
    classes_object = ClassesService()
    def get(self, request,class_id):
        start_get = time.time()
        print("started")
        try:
            data = self.classes_object.fetch_class_performance(class_id)
            print("abc")
            return Response(data, status=status.HTTP_200_OK, headers=None)
        # Handling excepitons
        except Exception as e:
            print(traceback.format_exc())
        
        finally:
            self.log.info("END : {0}".format(time.time()))
            self.log.info("Total execution time : {0}".format(time.time()-start_get))


class DetailedScoresController(views.APIView):

    log = logging.getLogger(__name__)
    students_object = StudentsService()
    def get(self, request,class_id,student_id):
        start_get = time.time()
        print("started")
        print("student_id>>>>>>>>>",student_id)
        try:
            data = self.students_object.get_detailed_result(student_id,class_id)    
            return Response(data, status=status.HTTP_200_OK, headers=None)
        # Handling excepitons
        except Exception as e:
            print(traceback.format_exc())
        
        finally:
            self.log.info("END : {0}".format(time.time()))
            self.log.info("Total execution time : {0}".format(time.time()-start_get))
