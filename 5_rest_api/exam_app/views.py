from rest_framework import viewsets, mixins
from .models import School, Classroom, Teacher, ClassroomTeacher, Student
from .serializers import SchoolSerializer, ClassroomSerializer, TeacherSerializer, ClassroomTeacherSerializer, StudentSerializer, ClassroomTeacherCreateSerializer
from django.db.models import Count
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

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
    #queryset = Classroom.objects.all()
    queryset = Classroom.objects.prefetch_related('classroomteacher_set__teacher')
    queryset = Classroom.objects.prefetch_related('students')
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

    filter_backends = [SearchFilter, DjangoFilterBackend]  # add search filter
    search_fields = ['classroomteacher__classroom__school__name']
    filterset_fields = ['name', 'lastname', 'gender']
    

    def get_queryset(self):
        queryset = self.queryset
        school_name = self.request.query_params.get('classroomteacher__classroom__school__name')
        #classroom_level= self.request.query_params.get('classroom_level')
        name = self.request.query_params.get('name')
        lastname = self.request.query_params.get('lastname')
        gender = self.request.query_params.get('gender')
        
        if school_name:

            queryset = queryset.filter(classroomteacher__classroom__school__name__icontains=school_name)
        #if classroom_level:
            #queryset = queryset.filter(classroom__level__icontains=school_name)
        if name:  # check if have parameter name
            queryset = queryset.filter(name__icontains=name) # like
        if lastname:  # check if have parameter name
            queryset = queryset.filter(lastname__icontains=lastname) # like
        if gender:  # check if have parameter name
            queryset = queryset.filter(gender__icontains=gender) # like
        
        return queryset


class ClassroomTeacherViewSet(viewsets.ModelViewSet):
    queryset = ClassroomTeacher.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ClassroomTeacherCreateSerializer
        return ClassroomTeacherSerializer
    

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = [SearchFilter]
    search_fields = ['classroom__school__name', 'name', 'lastname', 'gender']

    def get_queryset(self):
        queryset = self.queryset
        name = self.request.query_params.get('name')
        lastname = self.request.query_params.get('lastname')
        gender = self.request.query_params.get('gender')

        school_name = self.request.query_params.get('classroom__school__name')
        
        if name: 
            queryset = queryset.filter(name__contains=name) # like
        if lastname: 
            queryset = queryset.filter(lastname__icontains=lastname) # like
        if gender:
            queryset = queryset.filter(gender__icontains=gender) # like

        if school_name:
            queryset = queryset.select_related('classroom__school').filter(classroom__school__name__icontains=school_name) # like
            #queryset = Student.objects.select_related('classroom__school').filter(classroom__school__name__icontains="ชื่อโรงเรียน")
        print(str(queryset.query))
        return queryset


