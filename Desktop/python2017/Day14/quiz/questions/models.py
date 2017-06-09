from django.db import models

# Create your models here.

class Person(models.Model):
    years = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roll_no = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    joining_date = models.DateField(null=True)
    graduated = models.NullBooleanField(null=True)
    year = models.CharField(choices=years,max_length=30)
    class_room = models.ForeignKey('ClassRoom',on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name+" "+self.last_name

class ClassRoom(models.Model):
    name = models.CharField(max_length=30)
    time = models.TimeField(null=True)

    def __str__(self):
        return self.name




