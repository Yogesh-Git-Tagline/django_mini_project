from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField()
    contact_number = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='student_images/')