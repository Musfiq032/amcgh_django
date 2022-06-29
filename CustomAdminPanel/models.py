from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Doctor"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class AdminHOD(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Departments(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    department_short_description = models.CharField(max_length=255)
    department_description = RichTextField(blank=True, null=True)
    department_image = models.FileField(upload_to='department')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Doctors(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    degree = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    profile_pic = models.FileField()
    address = models.TextField()
    research_publication = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class ManagementTeam(models.Model):
    id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    profile_pic = models.FileField()
    objects = models.Manager()


class GoverningBody(models.Model):
    id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    objects = models.Manager()


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=255)
    service_description = RichTextField(blank=True, null=True)
    service_image = models.FileField(upload_to='service')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)

        if instance.user_type == 2:
            Doctors.objects.create(admin=instance, department_id=Departments.objects.get(id=1), address="",
                                   profile_pic="", gender="")


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.doctors.save()
