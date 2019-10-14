from university.settings import db
from bson.json_util import dumps
from pprint import pprint

class StudentsService:

    def fetch_all_students(self):
        all_students = db["students"].aggregate([
        {
            "$project": {
                "_id":0,
                "student_id": "$_id",
                "student_name": "$name"
            }
        }
        ])
        # all_students = db["students"].find({})
        return list(all_students)

    def get_classes_for_student(self,student_id):

        print("service entered")
        classes_for_each_student = db["grades"].aggregate([                
                {
                    "$match":{
                        "student_id":student_id
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
                    "$group":
                    {
                        "_id": { "student_id": "$student_id", "student_name": "$student_info.name" },
                        "classes": { "$addToSet": { "class_id": "$class_id" } }
                    }
                },
                {
                    "$project":
                    {
                        "classes": 1,
                        "student_id": "$_id.student_id",
                        "student_name": "$_id.student_name",
                        "_id": 0
                    }
                }
            ])
        return list(classes_for_each_student)

    def get_students_performance(self,student_id):
        performance_list = db["grades"].aggregate([
            {
                "$match":{
                    "student_id":student_id
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
                    "_id": { "student_id": "$student_id", "student_name": "$student_info.name", "class_id": "$class_id" },
                    "total_score": { "$sum": "$scores.score" }
                }
            },
            {
                "$group":
                {
                    "_id": { "student_id": "$_id.student_id", "student_name": "$_id.student_name" },
                    "classes": { "$push": { "class_id": "$_id.class_id", "total_marks": "$total_score" } }
                }
            },
            {
                "$project": {

                    "classes": 1,
                    "student_name": "$_id.student_name",
                    "student_id": "$_id.student_id",
                    "_id": 0
                }
            }
        ])

        # pprint(list(performance_list))
        performance_list = list(performance_list)
        # all_students = db["students"].find({})

        
        for each_class in  performance_list[0]["classes"]:
            each_class["total_marks"] = round(each_class["total_marks"])

        return performance_list[0]

    def get_detailed_result(self,student_id,class_id):
        student_obj = db["grades"].aggregate([
            {
                "$match":{
                    "class_id":class_id,
                    "student_id":student_id
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
               "$unwind":"$student_info"            
           },
           {
               "$project":
               {
                   "_id":0,
                   "student_id":1,
                   "student_name":"$student_info.name",
                   "scores":1,
                   "class_id":1,
                }
           },
           {
               "$unwind":"$scores"
           },
           {
                "$group":
                {
                    "_id": { "class_id": "$class_id" ,"student_id":"$student_id","student_name":"$student_name"},
                    "scores": { "$push": { "type": "$scores.type" ,"marks":"$scores.score"} }
                }
            },
            {
               "$project":
               {
                   "_id":0,
                   "student_id":"$_id.student_id",
                   "student_name":"$_id.student_name",
                   "class_id":"$_id.class_id",
                   "scores":1,
                   
                }
           }
        ])
        student_obj = list(student_obj)
        for each_type in student_obj[0]["scores"]:
            each_type["marks"] = round(each_type["marks"])
            
        return student_obj[0]
        
    def get_coll_data(self,name):
        # return dumps(list(db[name].find({}).limit(2)))
        return []