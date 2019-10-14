from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status
from ..services.student_service import StudentsService
import logging
import time
from bson.json_util import dumps
import traceback
# Create your views here.

class AllStudentsController(views.APIView):

    log = logging.getLogger(__name__)
    students_object = StudentsService()
    def get(self, request):
        start_get = time.time()
        print("started")
        try:
            data = self.students_object.fetch_all_students()
            print("abc")
            return Response(data, status=status.HTTP_200_OK, headers=None)
        # Handling excepitons
        except Exception as e:
            print(traceback.format_exc())
        
        finally:
            self.log.info("END : {0}".format(time.time()))
            self.log.info("Total execution time : {0}".format(time.time()-start_get))

class StudentsClassesController(views.APIView):

    log = logging.getLogger(__name__)
    students_object = StudentsService()
    def get(self, request,student_id):
        start_get = time.time()
        print("started")
        print("student_id>>>>>>>>>",student_id)
        try:
            data = self.students_object.get_classes_for_student(student_id)    
            return Response(data, status=status.HTTP_200_OK, headers=None)
        # Handling excepitons
        except Exception as e:
            print(traceback.format_exc())
        
        finally:
            self.log.info("END : {0}".format(time.time()))
            self.log.info("Total execution time : {0}".format(time.time()-start_get))

class StudentsPerformanceController(views.APIView):

    log = logging.getLogger(__name__)
    students_object = StudentsService()
    def get(self, request,student_id):
        start_get = time.time()
        print("started")
        print("student_id>>>>>>>>>",student_id)
        try:
            data = self.students_object.get_students_performance(student_id)    
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
    def get(self, request,student_id,class_id):
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


class DbController(views.APIView):

    log = logging.getLogger(__name__)
    students_object = StudentsService()
    def get(self, request):
        start_get = time.time()
        print("started")
        try:
            data = self.students_object.get_coll_data("grades")
            print("abc")
            data = {
                "message":"Congratulations! Your api is working successfully. Use the following endpoints for testing",
                "endpoints":[
                    "/students",
                    "/student/{student_id}/classes",
                    "/student/{student_id}/performance",
                    "/classes",
                    "/class/{class_id}/performance",
                    "/class/{class_id}/student/{student_id}",
                    "/student/{student_id}/class/{class_id}"
                    ]
            }
            return Response(data, status=status.HTTP_200_OK, headers=None)
        # Handling excepitons
        except Exception as e:
            print(traceback.format_exc())
        
        finally:
            self.log.info("END : {0}".format(time.time()))
            self.log.info("Total execution time : {0}".format(time.time()-start_get))
