from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField()
    email = models.EmailField()
    web = models.URLField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
