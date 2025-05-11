from django.db import models
from cloudinary.models import CloudinaryField # type: ignore

class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo =  CloudinaryField('image')
    class Meta:
        db_table = 'brand'
    def __str__(self):
        return self.name