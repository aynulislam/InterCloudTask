from django.db import models
from users.models import AuthUser
# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BookWishList(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)