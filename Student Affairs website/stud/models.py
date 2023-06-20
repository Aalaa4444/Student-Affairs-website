from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from pkg_resources import require

# Create your models here.

class studDetail(models.Model):
    Male = 'Male'
    FeMale = 'Female'
    GENDER_CHOICES = (
    (Male, 'Male'),
    (FeMale, 'Female'),
    )
    First = 'First' 
    Second = 'Second'
    Third = 'Third'
    Fourth ='Fourth'
    LEVEL_CHOICES = (
    (First, 'First'),
    (Second, 'Second'),
    (Third, 'Third'),
    (Fourth, 'Fourth'),
    )
    Active = 'Active'
    Unactive = 'Unactive'
    STATUS_CHOICES = (
    (Active, 'Active'),
    (Unactive, 'Unactive'),
    )
    CS = 'Computer Sceince' 
    IT = 'Information Technology'
    IS = 'Information System'
    AI ='Artificial Intelligence'
    DEPART_CHOICES = (
    (CS, 'Computer Sceince'),
    (IT, 'Information Technology'),
    (IS, 'Information System'),
    (AI, 'Artificial Intelligence'),
    )
    STUDENT_ID = models.IntegerField(unique=True)
    Fname = models.CharField(max_length=50, blank = False, null = False)
    Lname = models.CharField(max_length=50, blank = False, null = False)
    
    birthDate = models.DateField(default=timezone.now)
    #birthDate = models.DateField(default=timezone.now, validators=[MaxValueValidtaor(limit_value=date.today)])
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES, default = Male)
    gpa = models.FloatField(default=0)
    level = models.CharField(max_length = 10, choices = LEVEL_CHOICES, default = First)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES, default = First)
    depart = models.CharField(max_length = 50, choices = DEPART_CHOICES, default = AI)
    email = models.EmailField(max_length=25)
    phone = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title
    
  
class studing(models.Model):
    studedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    studedstud = models.ForeignKey(studDetail, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (
            ('studedBy', 'studedstud'),
        )

    def __str__(self):
        return str(self.studedBy) + str(self.studedstud)
