# from datetime import datetime
# from django.db import models
# from django.urls import reverse
# from PIL import Image
# from ckeditor.fields import RichTextField
#
#
# class Degree(models.Model):
#     degree_name = models.CharField(max_length=50, null=False)
#
#     def __str__(self):
#         return self.degree_name
#
#
# class Department(models.Model):
#     name = models.CharField(max_length=50)
#     department_image = models.ImageField(upload_to='department_image', default='default.png')
#     short_description = models.CharField(max_length=250, default='Nothing Found')
#     description = models.TextField(blank=False, default='Nothing Found')
#     published = models.DateTimeField(default=datetime.now)
#
#     def __str__(self):
#         return self.name
#
#     def save(self, **kwargs):
#         super().save()
#
#         img = Image.open(self.department_image.path)
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.department_image.path)
#
#     def get_absolute_url(self):
#         return reverse("Doctor:department-detail", kwargs={"id": self.id})
#
#
# class Doctor(models.Model):
#     title = models.CharField(max_length=100, blank=False)
#     Designation = models.CharField(blank=False, null=True, max_length=100)
#     doctor_image = models.ImageField(upload_to='doctor_profile_image', default='default.png')
#     Degree = models.ManyToManyField(Degree, blank=False)
#     contact = models.EmailField(max_length=254, blank=False)
#     department = models.ForeignKey(Department, blank=False, null=False, on_delete=models.CASCADE)
#     research_publications = RichTextField(blank=True, null=True)
#     visiting_time = models.CharField(max_length=254, blank=False)
#     published = models.DateTimeField(default=datetime.now)
#
#     def save(self, **kwargs):
#         super().save()
#
#         img = Image.open(self.doctor_image.path)
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.doctor_image.path)
#
#     def __str__(self):
#         return self.title
#
#
# # Create your models here.
# class Author(models.Model):
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.name
#
#
# class news(models.Model):
#     title = models.CharField(max_length=120)
#     news_image = models.ImageField(upload_to="Newsevents", default='default.png')
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     description = RichTextField(default='No Information Available', blank=False, null=False)
#     categories = models.ManyToManyField(Category)
#     publish_date = models.DateTimeField()
#     views = models.IntegerField(default=0)
#     reviewed = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse("Newsevents:news-details", kwargs={"id": self.id})
#
#
# class service(models.Model):
#     service_name = models.CharField(max_length=50)
#     service_short_description = models.CharField(max_length=500)
#     service_description = models.TextField(blank=False, null=False)
#     service_image = models.ImageField(upload_to='Service', default='medical_oncology.jpg')
#
#     def get_absolute_url(self):
#         return reverse("Service:service-detail", kwargs={"id": self.id})  # /* dynamic url */
#
#     def __str__(self):
#         return self.service_name
