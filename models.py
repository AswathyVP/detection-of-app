from django.db import models

# Create your models here.
class App(models.Model):
    appname=models.CharField(max_length=50)
    description=models.CharField(max_length=250)
    developer=models.CharField(max_length=250)
    size=models.CharField(max_length=50)
    def __str__(self):
        return self.appname

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Review(models.Model):
     appname=models.ForeignKey(App,related_name='app',on_delete=models.CASCADE)
     username=models.ForeignKey(User,related_name='uname',on_delete=models.CASCADE)
     review=models.CharField(max_length=250)
     rating=models.CharField(max_length=250)
     

class blockwords(models.Model):
    blockwords=models.CharField(max_length=50)
    def __str__(self):
        return self.blockwords