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

## 🎓 Courses
- Add Course
POST /api/courses/
- Get All Courses
GET /api/courses/
- Get Single Course
GET /api/courses/<course_id>/
- Edit Course
PUT /api/courses/<course_id>/
- Delete Course
DELETE /api/courses/<course_id>/

## 👨‍🏫 Teachers
- Add Teacher
POST /api/teachers/
- Get All Teachers
GET /api/teachers/
- Get Single Teacher
GET /api/teachers/<teacher_id>/
- Edit Teacher
PUT /api/teachers/<teacher_id>/
- Delete Teacher
DELETE /api/teachers/<teacher_id>/

## 🧑‍🎓 Students
- Add Student
POST /api/students/
- Get All Students
GET /api/students/
- Get Single Student
GET /api/students/<student_id>/
- Edit Student
PUT /api/students/<student_id>/
- Delete Student
DELETE /api/students/<student_id>/

## 📚 Enrollments
- Add Enrollment
POST /api/enrollments/
- Get All Enrollments
GET /api/enrollments/
- Get Single Enrollment
GET /api/enrollments/<enrollment_id>/
- Edit Enrollment
PUT /api/enrollments/<enrollment_id>/
- Delete Enrollment
DELETE /api/enrollments/<enrollment_id>/

## 📈 Progress
- Add Progress
POST /api/progress/
- Get All Progress
GET /api/progress/
- Get Single Progress
GET /api/progress/<progress_id>/
- Edit Progress
PUT /api/progress/<progress_id>/
- Delete Progress
DELETE /api/progress/<progress_id>/

## 📝 Reviews
- Add Review
POST /api/reviews/
- Get All Reviews
GET /api/reviews/
- Get Single Review
GET /api/reviews/<review_id>/
- Edit Review
PUT /api/reviews/<review_id>/
- Delete Review
DELETE /api/reviews/<review_id>/

## 🔒 Notes
- Ensure you configure authentication (e.g., token or session-based) for secure production use.
- The current setup is for development/testing purposes.
- You might consider pagination, filtering, and permissions for large-scale usage.
