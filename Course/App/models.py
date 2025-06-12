from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    availability = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    subjects = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Courses(models.Model):
    name = models.CharField(max_length=100)
    lesson = models.CharField(max_length=200)
    section = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Enrollment(models.Model):
    duration = models.CharField(max_length=100)
    started_at= models.DateTimeField(auto_created=True)
    endtime_at = models.DateTimeField()

class Progress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    completed = models.TextField()
    progress_point = models.FloatField(default=0.0)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s progress in {self.course.name}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

