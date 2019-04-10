from django.db import models

# Create your models here.
# Model for teachers
class Teacher(models.Model):
    teachers_name = models.CharField(max_length=30)
    academic_qualification = models.CharField(max_length=20)
    teaching_subject = models.CharField(max_length=20,blank=True)
    teachers_description = models.CharField(max_length=2000)
    teachers_photo = models.ImageField('photos/%Y/%m/%d/',blank=True)
    teachers_joining_date = models.DateField()
    teachers_contact_no = models.TextField()
    teachers_address = models.CharField(max_length=100,blank=True)

    # Lets define the main field of the listing model
    def __str__(self):
        return self.teachers_name  # will return the string representation of TEACHER
