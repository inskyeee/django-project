from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_number = models.CharField(max_length=20)
    email = models.EmailField()
    grades = models.TextField()
    satisfaction = models.CharField(max_length=20)
    improvements = models.TextField(blank=True)

    def __str__(self):
        return self.name
