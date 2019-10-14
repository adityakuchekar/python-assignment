def func_Q1(database_object):
    distinct_students = database_object["students"].distinct("_id")
    return len(list(distinct_students))

def func_Q2(database_object):
    distinct_students = database_object["grades"].distinct("class_id")
    return len(list(distinct_students))
