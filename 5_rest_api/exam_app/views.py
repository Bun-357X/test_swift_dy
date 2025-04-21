from rest_framework import viewsets, mixins
from .models import School, Classroom, Teacher, ClassroomTeacher, Student
from .serializers import SchoolSerializer, ClassroomSerializer, TeacherSerializer, ClassroomTeacherSerializer, StudentSerializer, ClassroomTeacherCreateSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class ClassroomTeacherViewSet(viewsets.ModelViewSet):
    queryset = ClassroomTeacher.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ClassroomTeacherCreateSerializer
        return ClassroomTeacherSerializer
    

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    


