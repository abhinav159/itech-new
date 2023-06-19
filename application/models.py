from django.db import models

# Create your models here.
class Student_details(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.EmailField(blank=False)
    phone = models.BigIntegerField(blank=False)
    date = models.DateField()
    gender = models.CharField(max_length=20)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    course = models.CharField(max_length=30)
    qualification = models.CharField(max_length=30)
    parent_number = models.BigIntegerField()
    postal = models.BigIntegerField()
    referal = models.CharField(max_length=30,default="")

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=False)
    telephone = models.BigIntegerField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Cards(models.Model):
    image=models.ImageField(upload_to='')
    heading=models.CharField(max_length=30,blank=False)
    sub_heading=models.CharField(max_length=30,blank=False)
    text1=models.TextField(blank=False)
    text2=models.TextField(blank=False)
    fees=models.IntegerField(blank=False)
    offerfees=models.IntegerField(blank=True,default='0')
    duration=models.IntegerField(blank=False)
    

    def __str__(self):
        return self.heading
    

class User_details(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(blank=False)
    phone = models.BigIntegerField()


    def __str__(self):
        return self.username
    


class Course_details(models.Model):
    date = models.DateField(blank=False)
    heading = models.CharField(max_length=40)
    para = models.CharField(max_length=200)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.heading
