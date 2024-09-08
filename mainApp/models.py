from django.db import models
from datetime import date

class ToDo(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Description = models.TextField(blank=True)
    Date = models.DateField(default=date.today)  

    def __str__(self):
        return self.Title 