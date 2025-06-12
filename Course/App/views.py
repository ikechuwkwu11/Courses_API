from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Courses,Teacher,Student,Enrollment,Progress,Review
from django.contrib.auth import logout
from .serializers import RegisterSerializer,LoginSerializer,TeacherSerializer,StudentSerializer,CoursesSerializer,EnrollmentSerializer,ProgressSerializer,ReviewsSerializer
from rest_framework import status

class Register(APIView):
    def post(self,request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully registered. Now Login!'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Login(APIView):
    def post(self,request):
        try:
            serializer= LoginSerializer(data=request.data)
            if serializer.is_valid():
                return Response({'message':'You have successfully logged in!!'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal Server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Logout(APIView):
    def get(self,request):
        try:
            logout(request)
            return Response({'message':'You have successfully logout!'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddCourses(APIView):
    def post(self,request):
        try:
            serializer = CoursesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your courses has been added'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetCourses(APIView):
    def get(self,request):
        try:
            course = Courses.objects.all()
            serializer = CoursesSerializer(course, many=True)
            return Response({'message':'This is all the courses','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleCourses(APIView):
    def get(self,request,courses_id):
        try:
            course = Courses.objects.get(id=courses_id)
            serializer = CoursesSerializer(course)
            return Response({'message':'This is the course','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditCourses(APIView):
    def put(self,request,courses_id):
        try:
            course = Courses.objects.get(id=courses_id)
            serializer = CoursesSerializer(course, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'This courses has been edited'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteCourses(APIView):
    def delete(self,request,courses_id):
        try:
            course = Courses.objects.get(id=courses_id)
            course.delete()
            return Response({'message':'This courses has been delete'},status=status.HTTP_200_OK)
        except Courses.DoesNotExist:
            return Response({'message':'This course is not available'})
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddTeacher(APIView):
    def post(self,request):
        try:
            serializer= TeacherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'This teacher has been added','data':serializer.data},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetTeacher(APIView):
    def get(self,request):
        try:
            teacher = Teacher.objects.all()
            serializer = TeacherSerializer(teacher, many=True)
            return Response({'message':'This are all the teachers','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleTeacher(APIView):
    def get(self,request,teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            serializer = TeacherSerializer(teacher)
            return Response({'message':'This is the data for this particular teacher','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditTeacher(APIView):
    def put(self,request,teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            serializer = TeacherSerializer(teacher,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'The teacher has been edited','data':serializer.data},status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteTeacher(APIView):
    def delete(self,request,teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            teacher.delete()
            return Response({'message':'This teacher has been deleted'})
        except Courses.DoesNotExist:
            return Response({'message':'This course is not available'})
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddStudent(APIView):
    def post(self,request):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'This student has been added'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetStudent(APIView):
    def get(self,request):
        try:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response({'message':'This is are all the students','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleStudent(APIView):
    def get(self,request,student_id):
        try:
            student = Student.objects.get(id=student_id)
            serializer = StudentSerializer(student)
            return Response({'message':'This is the data of this particular student','data':serializer.data},status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({'message':'This student does not exist'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditStudent(APIView):
    def put(self,request,student_id):
        try:
            student = Student.objects.get(id= student_id)
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message this student has been updated'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteStudent(APIView):
    def delete(self,request,student_id):
        try:
            student = Student.objects.get(id = student_id)
            student.delete()
            return Response({'message':'This student has been deleted'},status=status.HTTP_404_NOT_FOUND)
        except Student.DoesNotExist:
            return Response({'message':'This student does not exist'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddEnrollment(APIView):
    def post(self,request):
        try:
            serializer = EnrollmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your enrollment has been added'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetEnrollment(APIView):
    def get(self,request):
        try:
            enrollment = Enrollment.objects.all()
            serializer = EnrollmentSerializer(enrollment, many=True)
            return Response({'message':'This are all the enrollments','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleEnrollment(APIView):
    def get(self,request,enrollment_id):
        try:
            enrollment = Enrollment.objects.get(id=enrollment_id)
            serializer = EnrollmentSerializer(enrollment)
            return Response({'message':'This is the enrollment for this particular student','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditEnrollment(APIView):
    def put(self,request,enrollment_id):
        try:
            enrollment = Enrollment.objects.get(id = enrollment_id)
            serializer = EnrollmentSerializer(enrollment,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'This enrollment has been edited'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteEnrollment(APIView):
    def delete(self,request,enrollment_id):
        try:
            enrollment = Enrollment.objects.get(id = enrollment_id)
            enrollment.delete()
            return Response({'message':'This enrollment has been deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddProgress(APIView):
    def post(self,request):
        try:
            serializer = ProgressSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your progress has been added'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetProgress(APIView):
    def get(self,request):
        try:
            progress = Progress.objects.all()
            serializer= ProgressSerializer(progress, many=True)
            return Response({'message':'This are the progress datas','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleProgress(APIView):
    def get(self,request,progress_id):
        try:
            progress = Progress.objects.get(id=progress_id)
            serializer = ProgressSerializer(progress)
            return Response({'message':'This is the data','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditProgress(APIView):
    def put(self,request,progress_id):
        try:
            progress = Progress.objects.get(id=progress_id)
            serializer = ProgressSerializer(progress,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your progress has been edited'},status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteProgress(APIView):
    def delete(self,request,progress_id):
        try:
            progress = Progress.objects.get(id=progress_id)
            progress.delete()
            return Response({'message':'Your progress has been deleted'},status=status.HTTP_200_OK)
        except Progress.DoesNotExist:
            return Response({'message':'This id does not exist'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddReview(APIView):
    def post(self,request):
        try:
            serializer = ReviewsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'This Review has been added'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetReview(APIView):
    def get(self,request):
        try:
            review = Review.objects.all()
            serializer = ReviewsSerializer(review, many=True)
            return Response({'message':'This are all the reviews','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleReview(APIView):
    def get(self,request,review_id):
        try:
            review = Review.objects.get(id=review_id)
            serializer = ReviewsSerializer(review)
            return Response({'message':'This is the single Review','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditReview(APIView):
    def put(self,request,review_id):
        try:
            review = Review.objects.get(id=review_id)
            serializer = ReviewsSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your Review has been updated'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_404_NOT_FOUND)

class DeleteReview(APIView):
    def delete(self,request,review_id):
        try:
            review = Review.objects.get(id=review_id)
            review.delete()
            return Response({'message':'This review has been deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)