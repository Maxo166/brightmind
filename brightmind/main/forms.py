from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1']


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['title', 'description', 'poster_url', 'category']


class ChapterForm(forms.ModelForm):
    class Meta:
        model = models.Chapter
        fields = ['title', 'description', 'course']
