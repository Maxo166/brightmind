from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    poster_url = models.ImageField(
        upload_to="media\images\posters", height_field=None, width_field=None, max_length=None)
    category = models.ForeignKey("Category", related_name="courses", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)
    modifed_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"pk": self.pk})


class Chapter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    course = models.ForeignKey(
        Course, related_name='chapters', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=False)
    modifed_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Chapter_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categiry_name = models.CharField(max_length=50)
    categiry_description = models.TextField()
    reated_at = models.DateTimeField(auto_now_add=False)
    modifed_at = models.DateTimeField(auto_now=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


# class Sub_category(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     categiry_name = models.CharField(max_length=50)
#     reated_at = models.DateTimeField(auto_now_add=False)
#     modifed_at = models.DateTimeField(auto_now=False)

#     class Meta:
#         verbose_name_plural = "Sub_categories"

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("Sub_category_detail", kwargs={"pk": self.pk})


# class Field_category(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=False)
#     modifed_at = models.DateTimeField(auto_now=False)

#     class Meta:
#         verbose_name_plural = "Field_categories"

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("Field_category_detail", kwargs={"pk": self.pk})


class Tutorial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, related_name="tutorials", on_delete=models.CASCADE)
    poster_url = models.ImageField(
        upload_to="media\images\posters", height_field=None, width_field=None, max_length=None)
    video_url = models.FileField(upload_to="media\tutorials\video", max_length=100,
                                 validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    created_at = models.DateTimeField(auto_now_add=False)
    modifed_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tutorial_detail", kwargs={"pk": self.pk})
