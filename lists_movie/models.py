from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.

class CommonFields(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=40, unique=True, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Director(CommonFields):
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'director'
        verbose_name_plural = 'directors'
        ordering = ['name']
        db_table = 'director_table'

class CoDirector(CommonFields):

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'co_director'
        verbose_name = 'co_director'
        verbose_name_plural = 'co_directors'
        ordering = ['name']

class Actor(CommonFields):

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'actor'
        verbose_name = 'actor'
        verbose_name_plural = 'actors'
        ordering = ['name']

class Movies(models.Model):
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
    direct = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movie_dir')
    codir = models.ManyToManyField(CoDirector, related_name='CoDirector')
    actors = models.ManyToManyField(Actor, related_name='movie_actor')


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-release_year']  # Latest movies first
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        db_table = 'movie_table'


    
