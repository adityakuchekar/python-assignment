# python-assignment


This is a RESTful API written in Django REST framework.

# Running the API

1. Clone the repo
```
git clone https://github.com/adityakuchekar/python-assignment.git

```
2. create a virtual env
```
python3 -m venv /path/to/new/virtual/environment
```
3. Activate the virtual env

4. Install the dependencies
```
pip install -r <path_to_requirements.txt>
```
5. Run the development server
```
python manage.py runserver
```

# Testing the API

Root URL : http://34.93.91.203

I have hosted the api on a vm instance on google cloud platform. Please use the following below endpoints for testing the api.

* /students
* /student/{student_id}/classes
* /student/{student_id}/performance
* /classes
* /class/{class_id}/performance
* /class/{class_id}/student/{student_id}
* /student/{student_id}/class/{class_id}



