# VAMK Database School Schedule

## Demo
Web client:	http://ngocminh9862.pythonanywhere.com
![vamk](https://user-images.githubusercontent.com/24993267/44193932-30e21500-a13d-11e8-9454-3ce7ee93e645.png)

## Requirements
python 3.6.4

## Setting Up
Double click the file setup.bat

## Run The App
Double click the file run.bat

## Self Assessment

Note:
```
(*)	Completed
(+)	Partly done
(-)	Not working
```

### Validation criteria
```
(*)	Database schema drawn with Visual Paradigm
(*)	Table names reasonable
(*)	Initial list of tables
(*)	Field names reasonable
(*)	Primary and foreign keys reasonable
(*)	MySQL database tables created
(*)	Data imported to the database
(+)	Some SQL-queries (sqlqueries.txt) implemented
	(*)	teaching by teacher per year like in Excel
	(*)	teaching by student group like in Excel
	(*)	Student groups by degree program
	(*)	Teachers by degree program
	(+)	Teaching by teacher per week (weeks)
		NOTE: I make this one to report teaching per period
(*)	RESTful interface
(*)	CRUD for teacher, group, course, degree program
(*)	User authentication
(+)	REST client will return JSON and XML
	NOTE: Not working on web client but on http://127.0.0.1:8000/REST only
	(+)	pip install djangorestframework-xml
	(+)	pip install djangorestframework-jsonapi
(-)	Change log of database
(*)	Web client
	(*)	browse lecturer, group of student, degree program, study plan
	(*)	insert new lecture, group, degree program, study plan
(+)	Reporting client by Web client
	(*)	teaching by teacher like in Excel
	(*)	teaching by student group like in Excel
	(*)	Student groups by degree program
	(-)	Teachers by degree program
	(+)	Teaching by teacher per week (weeks)
		NOTE: I make this one to report teaching per period
(-)	Copying a last year curriculum as template for a new year
(*)	Git project
	(*)	a setup.bat to make installation easy
	(*)	a run.bat to make running the app easy
(*)	OPTION: If you have time and energy you are welcome to deploy the app
```
