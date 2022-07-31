from django.db import models

# Create your models here.
class Student(models.Model):
    classes = [
        ('5th', 'Class 5th'),
        ('6th', 'Class 6th'),
        ('7th', 'Class 7th'),
        ('8th', 'Class 8th'),
        ('9th', 'Class 9th'),
        ('10th', 'Class 10th'),
    ]
    name = models.CharField(max_length=100, verbose_name='Student Name')
    email = models.EmailField(max_length=100, null=True)
    phone = models.IntegerField()
    grade = models.CharField(max_length=100, choices=classes)
    dob = models.DateField(auto_now_add=False, verbose_name='Date of Birth')
    marks =  models.IntegerField(verbose_name='Percentage')
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    enrolledDate = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.name