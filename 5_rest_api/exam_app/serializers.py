from rest_framework import serializers
from .models import School, Classroom, Teacher, ClassroomTeacher, Student

class ClassroomSerializer(serializers.ModelSerializer):
    #school = SchoolSerializer()  #
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())

    class Meta:
        model = Classroom
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    classroom_count = serializers.IntegerField(read_only=True)
    student_count = serializers.IntegerField(read_only=True)
    teacher_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = School
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    
class StudentSerializer(serializers.ModelSerializer):
    #classroom = ClassroomSerializer()  #
    classroom = serializers.PrimaryKeyRelatedField(queryset=Classroom.objects.all())

    class Meta:
        model = Student
        fields = '__all__'


class ClassroomTeacherSerializer(serializers.ModelSerializer):
    classroom = serializers.StringRelatedField()
    teacher = serializers.StringRelatedField()

    class Meta:
        model = ClassroomTeacher
        fields = ['id', 'teacher', 'classroom']

class ClassroomTeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomTeacher
        fields = ['teacher', 'classroom']