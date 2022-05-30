from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Upload(models.Model):
    STATUS_CHOICES = (
        ('submitted','submitted'),
        ('pending','pending'),
        ('done','done'),
    )
    class Meta:
        verbose_name = 'Upload'
        verbose_name_plural = 'Uploads'
    date = models.DateField(auto_now_add=True)
    project_name = models.CharField(max_length=50)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=30,choices=STATUS_CHOICES,default='submitted')
    def __str__(self):
        return self.project_name

class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/', null=False,blank=False)


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Report(models.Model):
    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
    
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.ForeignKey(Upload,on_delete=models.CASCADE)
    report = models.FileField(upload_to='files/',blank=True)

    def __str__(self):
        return self.project_name.project_name
