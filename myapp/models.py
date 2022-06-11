from django.db import models

# Create your models here.


class Student(models.Model):

    book_name = models.CharField(max_length=200)

    author = models.CharField(max_length=100)

    published = models.CharField(max_length=60)

    class Meta:

        db_table = "Students_info"
