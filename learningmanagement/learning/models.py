from django.db import models
from django.contrib.auth.models import User


class instructorModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    specaility=models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.user.username}-({self.specaility})'
    
class studentModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.user.username}'

class Course(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()
    instructor=models.ForeignKey(instructorModel,on_delete=models.CASCADE,related_name='courses')
    def __str__(self) -> str:
        return f'{self.title}'

class Assignment(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()
    cource=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='assignments')
    def __str__(self) -> str:
        return f'{self.title}'
    
class Solution(models.Model):
    answer=models.TextField()
    assignment=models.OneToOneField(Assignment,on_delete=models.CASCADE,related_name='solutions')
    def __str__(self) -> str:
        return f'{self.answer}'