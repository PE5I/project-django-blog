from django.db import models
from tinymce.models import HTMLField

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()
    hyperlink = models.CharField(max_length=500)
    sorting_int = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['sorting_int',]