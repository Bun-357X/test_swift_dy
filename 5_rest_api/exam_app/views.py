from rest_framework import viewsets, mixins
from .models import School, Classroom, Teacher, ClassroomTeacher, Student
from .serializers import SchoolSerializer, ClassroomSerializer, TeacherSerializer, ClassroomTeacherSerializer, StudentSerializer, ClassroomTeacherCreateSerializer
from django.db.models import Count
from rest_framework.filters import SearchFilter

class SchoolViewSet(viewsets.ModelViewSet):
    #queryset = School.objects.all()
    #queryset = School.objects.prefetch_related('classrooms')
    
    serializer_class = SchoolSerializer

    queryset = School.objects.annotate(classroom_count=Count('classrooms'),
                                        student_count=Count('classrooms__students'),
                                        teacher_count=Count('classrooms__classroomteacher__teacher', distinct=True))# count ผ่านตารางกลาง

    filter_backends = [SearchFilter]  # add search filter
    search_fields = ['name']

    def get_queryset(self):
        queryset = self.queryset
        name = self.request.query_params.get('name')

        if name:  # check if have parameter name
            queryset = queryset.filter(name__icontains=name) # like

        return queryset

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    filter_backends = [SearchFilter]  # add search filter
    search_fields = ['school__name']

    def get_queryset(self):
        queryset = self.queryset
        school_name = self.request.query_params.get('school_name')

        if school_name:
            queryset = queryset.filter(school__name__icontains=school_name)# filter ตารางหลัก

        return queryset


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
    


