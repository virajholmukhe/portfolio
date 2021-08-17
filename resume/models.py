from django.core.checks import messages
from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table="Profile"

class Languages(models.Model):
    name = models.CharField(max_length=20)
    knowledge = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table="Languages"

class Project(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/projects")
    url = models.CharField(max_length=50,blank=True)
    repo = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table="Projects"

class Contact(models.Model):
    email = models.EmailField(max_length=50)
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table="Contact"

class ContactMe(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.email

    class Meta:
        db_table="ContactMe"