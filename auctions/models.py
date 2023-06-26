from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.category_name
        

class Bid(models.Model):
    bid = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="bidAuthor")

    def __str__(self) -> str:
        return str(self.bid)


class Listing(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    image_url = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)

    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="price")

    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="owner")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")

    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="watchlist")

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="author")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=True, null=True, related_name="listing")
    comment =  models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"{self.author}"


