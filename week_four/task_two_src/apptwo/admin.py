from django.contrib import admin
from . import models


myModel = [models.Student,models.Coach,models.Task]
admin.site.register(myModel)