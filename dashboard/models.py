from django.db import models
from django.contrib.auth.models import User


# NOTES SECTION MODEL
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"

# class Notes(models.Model): 
#    class Meta: verbose_name_plural = 'Notes'
        

#HOMEWORK SECTION MODEL
        
class Homework(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    


# TODOO SECTION MODEL
    

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    is_finished = models.BooleanField(default = False)

    def __str__(self):
        return self.title
    


# BOOK SECTION MODEL
    


