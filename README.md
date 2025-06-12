# 📚 Online Learning Platform API
This project is a Django REST Framework-based backend API designed for managing an online learning platform. It supports functionalities such as user registration/login, course management, teacher/student records, enrollment tracking, progress monitoring, and reviews.

## 🚀 Features
- User Registration and Login
- CRUD for Courses
- CRUD for Teachers
- CRUD for Students

## 📝 Enrollments Handling
- Student Progress Tracking
- Course Reviews Management
- Clean, RESTful API architecture

## 🛠️ Technologies Used
- Python 3.x
- Django
- Django REST Framework
- SQLite (default for development)

## 📦 API Endpoints
- Below are some of the available endpoints:

## 🔐 Auth
- Method	Endpoint	Description
- POST	/register/	Register a user
- POST	/login/	Login a user
- GET	/logout/	Logout user session

## 📘 Courses
- Method	Endpoint	Description
- POST	/courses/	Add a new course
- GET	/courses/	Get all courses
- GET	/courses/<id>/	Get a single course
- PUT	/courses/<id>/	Edit a course
- DELETE	/courses/<id>/	Delete a course

## 👩‍🏫 Teachers
- Method	Endpoint	Description
- POST	/teachers/	Add a new teacher
- GET	/teachers/	Get all teachers
- GET	/teachers/<id>/	Get a single teacher
- PUT	/teachers/<id>/	Edit a teacher
- DELETE	/teachers/<id>/	Delete a teacher

## 👨‍🎓 Students
- Method	Endpoint	Description
- POST	/students/	Add a new student
- GET	/students/	Get all students
- GET	/students/<id>/	Get a single student
- PUT	/students/<id>/	Edit a student
- DELETE	/students/<id>/	Delete a student

## 📝 Enrollment
- Method	Endpoint	Description
- POST	/enrollments/	Enroll a student
- GET	/enrollments/	Get all enrollments
- GET	/enrollments/<id>/	Get a single enrollment
- PUT	/enrollments/<id>/	Edit an enrollment
- DELETE	/enrollments/<id>/	Delete an enrollment

## 📊 Progress
- Method	Endpoint	Description
- POST	/progress/	Add student progress
- GET	/progress/	Get all progress records
- GET	/progress/<id>/	Get a single progress
- PUT	/progress/<id>/	Edit progress record
- DELETE	/progress/<id>/	Delete progress

## 🌟 Reviews
- Method	Endpoint	Description
- POST	/reviews/	Add a course review
- GET	/reviews/	Get all reviews
- GET	/reviews/<id>/	Get a single review
- PUT	/reviews/<id>/	Edit a review
- DELETE	/reviews/<id>/	Delete a review

## 🔒 Notes
- Ensure you configure authentication (e.g., token or session-based) for secure production use.
- The current setup is for development/testing purposes.
- You might consider pagination, filtering, and permissions for large-scale usage.
