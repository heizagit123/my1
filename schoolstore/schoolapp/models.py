from django.db import models



# class Form(models.Model):
#     name=models.CharField(max_length=250)
#     dob= models.DateField(null=True,blank=True)
#     age=models.IntegerField( )
#     gender = models.CharField(max_length=15)
#     phone=models.CharField(max_length=50 )
#     email=models.EmailField(max_length=200)
#     address=models.CharField(max_length=250)
#     department= models.CharField(max_length=250)
#     course = models.CharField(max_length=250)
#     purpose = models.CharField(max_length=250)
#     materials = models.CharField(max_length=250)
#
#
#     def __str__(self):
#         return self.name
#
#

class application(models.Model):
    name=models.CharField(max_length=250)
    dob= models.DateField(null=True,blank=True)
    age=models.IntegerField(blank=True,null=True)
    gender=models.CharField(max_length=250)
    phone=models.CharField(max_length=250 )
    email=models.EmailField(max_length=200)
    address=models.CharField(max_length=250)
    department= models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    purpose = models.CharField(max_length=250)
    materials = models.CharField(max_length=250)


    def __str__(self):
        return self.name




