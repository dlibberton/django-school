from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Grade(models.Model):
    grade = models.DecimalField(
        default=100.00,
        max_digits=5, 
        decimal_places=2, 
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        
        a_subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True, blank=True),
        
        student = models.ForeignKey('Student', on_delete=models.CASCADE, null=True, blank=True)
    )

    def __str__(self):
        return str(self.grade)