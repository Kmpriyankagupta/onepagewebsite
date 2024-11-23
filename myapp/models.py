from django.db import models
from django.contrib.auth.models import User



class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.CharField(max_length=50,blank=True,null=True)
    price = models.DecimalField(decimal_places=2, max_digits=6,blank=True,null=True)
    rating = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.title
    
class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')
    biography = models.TextField()
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.author.name}'s Profile"
    

class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # 'login' or 'logout'
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.action} at {self.timestamp}"
    

class cloths(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name
    




