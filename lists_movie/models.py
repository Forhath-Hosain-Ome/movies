from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
class movies(models.Model):
    genre_choices = [
        ('ACT', 'Action'),
        ('MYS', 'Mystery'),
        ('ADV', 'Adventure'),
    ]
    title = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=100)
    release_year = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(2026)]
    )
    is_available = models.BooleanField()
    genra = models.CharField(choices=genre_choices, max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Direc = models.ForeignKey(director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-release_year']  # Latest movies first
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        db_table = 'movie_table'

class director(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        varbosa_name = 'director'
        varbosa_name_plural = 'directors'
        ordering = ['name']
        db_table = 'director_table'
    
class co_director(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'co_director'
        verbosa_name = 'co_director'
        verbosa_name_plural = 'co_directors'
        ordering = ['name']