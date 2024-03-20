from django.db import models
from .validators import validate_name_format, validate_combination_format, validate_school_email
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, unique=False, validators=[validate_name_format])
    student_email = models.EmailField(unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(unique=True, blank=True, null=True)
    locker_number = models.IntegerField(unique=True, default=110, validators=[
            MinValueValidator(1, message='Ensure this value is greater than or equal to 1.'),
            MaxValueValidator(200, message="Ensure this value is less than or equal to 200.")
        ])
    locker_combination = models.CharField(max_length=20, unique=False, default="12-12-12", validators=[validate_combination_format])
    good_student = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, new_locker_number):
        self.locker_number = new_locker_number
        self.save()
        
    def student_status(self, is_good_student):
        self.good_student = is_good_student
        self.save()
        