from tkinter.font import names

from django.urls import path
from .views import Register,Login,Logout,AddCourses,GetCourses,EditCourses,DeleteCourses,SingleCourses,AddTeacher,GetTeacher,SingleTeacher,EditTeacher,DeleteTeacher,AddStudent,GetStudent,SingleStudent,EditStudent,DeleteStudent,AddEnrollment,GetEnrollment,SingleEnrollment,EditEnrollment,DeleteEnrollment,AddProgress,GetProgress,SingleProgress,EditProgress,DeleteProgress,AddReview,GetReview,SingleReview,EditReview,DeleteReview

urlpatterns =[
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('add_courses/',AddCourses.as_view(),name='add_courses'),
    path('get_courses/',GetCourses.as_view(),name='get_courses'),
    path('edit_courses/<int:courses_id>',EditCourses.as_view(),name='edit_courses'),
    path('delete_courses/<int:courses_id>',DeleteCourses.as_view(),name='delete_courses'),
    path('single_courses/<int:courses_id>',SingleCourses.as_view(),name='single_courses'),
    path('add_teacher/',AddTeacher.as_view(),name='add_teacher'),
    path('get_teacher/',GetTeacher.as_view(),name='get_teacher'),
    path('single_teacher/<int:teacher_id>',SingleTeacher.as_view(),name='single_teacher'),
    path('edit_teacher/<int:teacher_id>',EditTeacher.as_view(),name='edit_teacher'),
    path('delete_teacher/<int:teacher_id>',DeleteTeacher.as_view(),name='delete_teacher'),
    path('add_student/',AddStudent.as_view(),name='add_student'),
    path('get_student/',GetStudent.as_view(),name='get_student'),
    path('single_student/<int:student_id>',SingleStudent.as_view(),name='single_student'),
    path('edit_student/<int:student_id>',EditStudent.as_view(),name='edit_student'),
    path('delete_student/<int:student_id>',DeleteStudent.as_view(),name='delete_student'),
    path('add_enrollment/',AddEnrollment.as_view(),name = 'add_enrollment'),
    path('get_enrollment/',GetEnrollment.as_view(),name='get_enrollment'),
    path('single_enrollment/<int:enrollment_id>',SingleEnrollment.as_view(),name='single_enrollment'),
    path('edit_enrollment/<int:enrollment_id>',EditEnrollment.as_view(),name='edit_enrollment'),
    path('delete_enrollment/<int:enrollment_id>',DeleteEnrollment.as_view(),name='delete_enrollment'),
    path('add_progress/',AddProgress.as_view(),name='add_progress'),
    path('get_progress/',GetProgress.as_view(),name='get_progress'),
    path('single_progress/<int:progress_id>',SingleProgress.as_view(),name='single_progress'),
    path('edit_progress/<int:progress_id>',EditProgress.as_view(),name='edit_progress'),
    path('delete_progress/<int:progress_id>',DeleteProgress.as_view(),name='delete_progress'),
    path('add_review/',AddReview.as_view(),name='add_review'),
    path('get_review/',GetReview.as_view(),name='get_review'),
    path('single_review/<int:review_id>',SingleReview.as_view(),name='single_review'),
    path('edit_review/<int:review_id>',EditReview.as_view(),name='edit_review'),
    path('delete_review/<int:review_id>',DeleteReview.as_view(),name='delete_review')

]