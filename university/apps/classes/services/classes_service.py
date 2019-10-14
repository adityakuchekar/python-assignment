from university.settings import db
from bson.json_util import dumps
from pprint import pprint

class ClassesService:

    def fetch_all_classes(self):
        all_classes = db["grades"].distinct("class_id")
        all_classes = list(all_classes)
        # all_students = db["students"].find({})

        classes = [{"class_id":each_id} for each_id in all_classes]
        return classes


    def fetch_students_of_class(self,class_id):
        
        all_students = db["grades"].aggregate([
            {
                "$match":
                {
                    "class_id": class_id
                }
            },

            {
                "$group":
                {
                    "_id": { "class_id": "$class_id" },
                    "students": { "$addToSet": { "student_id": "$student_id" } }
                }
            },
            {
                "$lookup":
                {
                    "from": "students",
                    "localField": "students.student_id",
                    "foreignField": "_id",
                    "as": "student_info"
                }
            },
            {
                "$project":
                {
                    "students": 0,
                    "_id": 0
                }
            }
        ])
        all_students = list(all_students)

        for each_student in all_students[0]["student_info"]:
            each_student["student_name"] = each_student.pop("name")
            each_student["student_id"] = each_student.pop("_id")

        final_students = {
            "class_id":class_id,
            "students":all_students[0]["student_info"]
        }
        
        return final_students
    
    def fetch_class_performance(self,class_id):

        performance_list = db["grades"].aggregate([
            {
                "$match":{
                    "class_id":class_id
                    }            
            },
            {
                "$lookup":
                {
                    "from": "students",
                    "localField": "student_id",
                    "foreignField": "_id",
                    "as": "student_info"
                }
            },
            {
                "$unwind": "$student_info"
            },
            {
                "$unwind": "$scores"
            },
            {
                "$group":
                {
                    "_id": { "student_id": "$student_info._id","student_name":"$student.name" },
                    "total_marks": { "$sum": "$scores.score" }
                }
            },
            {
                "$project": {                 
                    "student_id": "$_id.student_id",
                    "total_marks":1,
                    "_id": 0
                }
            },
            {
                "$lookup":
                {
                    "from": "students",
                    "localField": "student_id",
                    "foreignField": "_id",
                    "as": "student_info"
                }
            },
        ])

        performance_list = list(performance_list)        

        for each_student in performance_list:
            each_student["student_name"] = each_student["student_info"][0]["name"]
            each_student["total_marks"] = round(each_student["total_marks"])
            each_student.pop("student_info")

        class_performance = {
            "class_id":class_id,
            "students":performance_list
        }
        # pprint(performance_list)
        return class_performance
        # for each_student in performance_list:

