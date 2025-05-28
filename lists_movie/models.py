from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
class movies(models.Model):
    genra_choice = [
        ('ACT', 'Action'),
        ('MYS', 'Mystery'),
        ('ADV', 'Adventure'),
    ]
    title = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=100)
    release_year = models.IntegerField(max_length=4)
    is_available = models.BooleanField()
    genra = models.CharField(choices=genra_choice, max_length=3)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-release_year']  # Latest movies first
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        db_table = 'movie_table'