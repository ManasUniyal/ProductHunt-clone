from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    url = models.TextField()
    votes_total = models.BigIntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='icons/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__ (self):
        return self.title

    def pub_date_pretty(self):
        return datetime.datetime.now().date()

    def summary(self):
        return self.body[:100]
