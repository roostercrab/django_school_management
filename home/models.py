from django.db import models

# Create your models here.
# Student Model
class Student(models.Model):
    # class attribute/fields  is here ---- Model fields
    students_name = models.CharField(max_length=30)
    students_id = models.IntegerField()
    students_class = models.CharField(max_length=20)
    students_roll = models.IntegerField()
    students_dob = models.DateField(blank=True)
    students_gender = models.CharField(max_length=10)
    students_gardian_name = models.CharField(max_length=30,blank=True)
    students_gardian_phone_no = models.IntegerField(blank=True)
    students_photo = models.ImageField('photos/%Y/%m/%d/',blank=True)
    students_opinion = models.CharField(max_length=1000,blank=True)
    students_address = models.CharField(max_length=100,blank=True)

    # Lets define the main field of the listing model
    def __str__(self):
        return self.students_name  # will return the string representation of students name


