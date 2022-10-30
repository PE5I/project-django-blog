from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    # content = HTMLField()
    content = RichTextField()
    created_at = models.DateTimeField(datetime.date.today())
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=40)

    # show or hide the blog post
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at',]
