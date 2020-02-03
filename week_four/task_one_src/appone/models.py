from django.db import models



class Student(models.Model):
    student_id = models.IntegerField()
    firstname = models.CharField(verbose_name='First Name', max_length=20)
    lastname = models.CharField(verbose_name='Last Name', max_length=20)
    message = models.TextField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.firstname, self.message)