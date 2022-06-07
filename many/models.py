from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    active = models.BooleanField(default=False)
    default_course = models.BooleanField(default=False)


class MyUser(User):
    courses = models.ManyToManyField(Courses, related_name="user_courses", blank=True)
