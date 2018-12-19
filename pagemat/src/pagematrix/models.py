from django.db import models

# Create your models here.
class pagematrix(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200)
    description = models.TextField(default = 'description default text')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Post(models.Model):
	name = models.TextField()
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=15)