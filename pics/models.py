from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    loc_name = models.CharField(max_length =30)

    def __str__(self):
        return self.loc_name

class Category(models.Model):
    cat_name = models.CharField(max_length =30)

    def __str__(self):
        return self.cat_name

class Image(models.Model):
    title = models.CharField(max_length =30)
    description = models.TextField(max_length =30)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING,)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, )
    pub_date = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.title

