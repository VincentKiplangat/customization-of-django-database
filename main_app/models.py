from django.db import models

# Create your models here.


# name, email, dob , salary, disabled
class Employee(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    salary = models.DecimalField(max_digits=12, decimal_places=2)  #67000.58
    disabled = models.BooleanField(default=False)
    profile = models.ImageField(upload_to="employees" , null=True)
    created_at = models. DateTimeField(auto_now_add=True, null=True) # Once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True) # Every time an update happens

    def __str__(self):
        return self.name



