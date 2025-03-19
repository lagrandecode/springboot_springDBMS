from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class BasePerson(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(120)
        ]
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(BasePerson):
    student_id = models.CharField(max_length=20, unique=True)
    grade = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12)
        ]
    )
    date_of_birth = models.DateField()
    address = models.TextField()
    parent_contact = models.CharField(max_length=15)

    class Meta:
        ordering = ['student_id']

class Teacher(BasePerson):
    teacher_id = models.CharField(max_length=20, unique=True)
    subject = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience_years = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(50)
        ]
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    class Meta:
        ordering = ['teacher_id']



# Path: api/serializers.py
