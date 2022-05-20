from signal import default_int_handler
from django.db import models

# Create your models here.
class Sticky(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title