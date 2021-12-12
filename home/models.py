from django.db import models
from django.contrib.auth.models import User
# Create your models here.


TYPE = (
    ('Postive', 'Postive'),
    ('Negavtive' , 'Negavtive')
    )

class Bill(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=256,default="")
    def __str__(self):
        return self.name
    

class Expense(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    expense_type = models.CharField(max_length=100 , choices=TYPE)
    
    
    def __str__(self):
        return self.name
    