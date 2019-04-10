from django.db import models

# Create your models here.
# Model for existing academic classes
class AcademicClasses(models.Model):
    # class attribute/fields  is here ---- Model fields
    class_name = models.CharField(max_length=30)
    No_of_students = models.IntegerField()
    class_description = models.CharField(max_length=2000)
    class_picture = models.ImageField('photos/%Y/%m/%d/',blank=True)
    class_coordinators = models.CharField(max_length=30)
    monthly_fee = models.IntegerField()
    available_seats = models.IntegerField()
    class_schedule = models.CharField(max_length=30)
    class_coordinators_phone_no = models.IntegerField()
    subjects_name = models.CharField(max_length=1000)

    # Lets define the main field of the listing model
    def __str__(self):
        return self.class_name  # will return the string representation of CLASS
