from django.db import models
from django.db.models.base import Model
from django.core.validators import MinLengthValidator
from django.db.models.deletion import CASCADE

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=25)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name + " "+self.last_name

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=150)
    image = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,null= True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title