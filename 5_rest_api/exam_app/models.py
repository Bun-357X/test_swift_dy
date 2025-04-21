from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    name_short = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    

class Classroom(models.Model):
    level = models.CharField(max_length=255)
    sub_level = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="classrooms")

    def __str__(self):
        return f"{self.level}/{self.sub_level}"
    
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    classroom = models.ManyToManyField(Classroom, through='ClassroomTeacher')

    def __str__(self):
        return self.name
    
class ClassroomTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'classroom')
    
class Student(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.name
