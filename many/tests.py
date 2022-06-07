from django.test import TestCase
from many.models import Courses, MyUser

# Create your tests here.
class TestModels(TestCase):
    def test_models(self):
        course_data = {
            "title": "Django",
            "description": "Django course",
            "active": True,
            "default_course": True,
        }
        course = Courses.objects.create(**course_data)
        user = MyUser.objects.create_user(username="test", password="test")
        user.courses.add(course)

        self.assertEqual(user.courses.count(), 1)

        self.assertEqual(user.courses.first().title, "Django")
        self.assertEqual(user.courses.first().description, "Django course")
        self.assertEqual(user.courses.first().active, True)
        self.assertEqual(user.courses.first().default_course, True)

        self.assertEqual(
            user.courses.first(), Courses.objects.filter(user_courses=user).first()
        )
