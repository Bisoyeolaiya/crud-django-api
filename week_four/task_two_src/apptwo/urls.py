from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'students', views.StudentView)
router.register(r'coachs', views.CoachView)
router.register(r'tasks', views.TaskView)


urlpatterns = [
    url(r'^api/', include(router.urls))
]
