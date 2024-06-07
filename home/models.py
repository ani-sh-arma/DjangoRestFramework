from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Person(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + str(self.age)
    