from django.db import models

class Roomie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name