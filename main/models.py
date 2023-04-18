from django.db import models

# Create your models here.
"""class Post(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)
    def comment_count(self):
        return self.comments.count()
    
    def __str__(self):
        return self.title
    def is_liked_by(self, user):
        return self.likes.filter(id=user.id).exists()"""


class Jeff(models.Model):
    image = models.ImageField()
