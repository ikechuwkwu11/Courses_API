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

## 🛠️ Tech Stack
| Layer       | Technology                                          |
| ----------- | --------------------------------------------------- |
| Language    | Python 3.x                                          |
| Framework   | Django, Django REST Framework                       |
| Database    | SQLite (for development)                            |
| Auth System | Session or Token-based (recommended for production) |


## 📦 API Endpoints
- Below are some of the available endpoints:

## 🔐 Auth
| Method | Endpoint     | Description      |
| ------ | ------------ | ---------------- |
| POST   | `/register/` | Register a user  |
| POST   | `/login/`    | Log in a user    |
| GET    | `/logout/`   | Log out the user |


## 🎓 Courses
| Method | Endpoint             | Description       |
| ------ | -------------------- | ----------------- |
| POST   | `/api/courses/`      | Add a new course  |
| GET    | `/api/courses/`      | List all courses  |
| GET    | `/api/courses/<id>/` | Get single course |
| PUT    | `/api/courses/<id>/` | Update a course   |
| DELETE | `/api/courses/<id>/` | Delete a course   |


## 👨‍🏫 Teachers
| Method | Endpoint              | Description        |
| ------ | --------------------- | ------------------ |
| POST   | `/api/teachers/`      | Add a teacher      |
| GET    | `/api/teachers/`      | List all teachers  |
| GET    | `/api/teachers/<id>/` | Get single teacher |
| PUT    | `/api/teachers/<id>/` | Update a teacher   |
| DELETE | `/api/teachers/<id>/` | Delete a teacher   |


## 🧑‍🎓 Students
| Method | Endpoint              | Description        |
| ------ | --------------------- | ------------------ |
| POST   | `/api/students/`      | Add a student      |
| GET    | `/api/students/`      | List all students  |
| GET    | `/api/students/<id>/` | Get single student |
| PUT    | `/api/students/<id>/` | Update a student   |
| DELETE | `/api/students/<id>/` | Delete a student   |


## 📚 Enrollments
| Method | Endpoint                 | Description          |
| ------ | ------------------------ | -------------------- |
| POST   | `/api/enrollments/`      | Add an enrollment    |
| GET    | `/api/enrollments/`      | List all enrollments |
| GET    | `/api/enrollments/<id>/` | Get one enrollment   |
| PUT    | `/api/enrollments/<id>/` | Update enrollment    |
| DELETE | `/api/enrollments/<id>/` | Delete enrollment    |


## 📈 Progress
| Method | Endpoint              | Description         |
| ------ | --------------------- | ------------------- |
| POST   | `/api/progress/`      | Add progress        |
| GET    | `/api/progress/`      | List progress       |
| GET    | `/api/progress/<id>/` | Get single progress |
| PUT    | `/api/progress/<id>/` | Update progress     |
| DELETE | `/api/progress/<id>/` | Delete progress     |


## 📝 Reviews
| Method | Endpoint             | Description      |
| ------ | -------------------- | ---------------- |
| POST   | `/api/reviews/`      | Add a review     |
| GET    | `/api/reviews/`      | List all reviews |
| GET    | `/api/reviews/<id>/` | Get a review     |
| PUT    | `/api/reviews/<id>/` | Update a review  |
| DELETE | `/api/reviews/<id>/` | Delete a review  |


## 🔒 Notes
- Ensure you configure authentication (e.g., token or session-based) for secure production use.
- The current setup is for development/testing purposes.
- You might consider pagination, filtering, and permissions for large-scale usage.
