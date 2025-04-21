from rest_framework import serializers
from .models import School, Classroom, Teacher, ClassroomTeacher, Student

class StudentSerializer(serializers.ModelSerializer):
    #classroom = ClassroomSerializer()  #

    class Meta:
        model = Student
        fields = '__all__'
        depth = 1
        depth = 2

class TeacherSerializer(serializers.ModelSerializer):
    classroom = serializers.SerializerMethodField()
    class Meta:
        model = Teacher
        fields = '__all__'
    def get_classroom(self, obj):
        return [{'id': c.id, 'level': c.level, 'sub_level': c.sub_level} for c in obj.classrooms_teachers.all()] 

class ClassroomSerializer(serializers.ModelSerializer):
    #school = SchoolSerializer()  #
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), required=False)
    students = StudentSerializer(many=True, required=False)
    teachers = TeacherSerializer(many=True, required=False)
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