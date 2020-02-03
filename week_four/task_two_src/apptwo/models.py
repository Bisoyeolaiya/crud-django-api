from django.db import models

class Student(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(verbose_name='First Name', max_length=30)
    last_name = models.CharField(verbose_name='Last Name', max_length=30)
    age = models.PositiveIntegerField(verbose_name='Age')
    email_address = models.EmailField(verbose_name='Email Address', max_length=150, unique=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=15)
    SEX = (
        ('m','Male'),
        ('f', 'Female')

    )

    sex = models.CharField(verbose_name='Gender/Sex', max_length=1, choices=SEX)

    COURSE = (
        ('web-dev', 'Web Development'),
        ('pub-hlth', 'Public Health'),
        ('data-lst', 'Data Analysis')
    )

    course = models.CharField(verbose_name='Course Title', max_length=10, choices=COURSE)

    def __str__(self):
        return '%s %s' % (self.first_name, self.course)



class Coach(models.Model):
    coach_id = models.IntegerField()
    first_name = models.CharField(verbose_name='First Name',max_length=30)
    last_name = models.CharField(verbose_name='Last Name', max_length=30)
    email_address = models.EmailField(verbose_name='Email Address', max_length=150, unique=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=15)

    def __str__(self):
        return self.first_name


class Task(models.Model):
    task_id =  models.IntegerField()
    task_title = models.CharField(verbose_name='Task Title', max_length=250)
    task_given = models.TextField(verbose_name='Task Given')
    task_startdate = models.DateField(verbose_name='Task Start Date')
    task_deadline = models.DateField(verbose_name='Task End Date')
    comment = models.TextField(verbose_name='Comment', max_length=500)

    def __str__(self):
        return self.task_title
