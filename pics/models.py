from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    loc_name = models.CharField(max_length =30)

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    
    def update_location(self,update):
        self.loc_name = update
        self.save()
    
    @classmethod
    def get_location_id(cls ,id):
        location = Location.objects.get(pk =id)
        return location

    def __str__(self):
        return self.loc_name

class Category(models.Model):
    cat_name = models.CharField(max_length =30)

    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.cat_name = update
        self.save()
    
    def get_category_id(cls, id):
        category = Category.object.get(pk = id)
        return category

    def __str__(self):
        return self.cat_name

class Image(models.Model):
    title = models.CharField(max_length =30)
    description = models.TextField(max_length =30)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING,)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, )
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'photos/', default='VALID PYTHON') 

    class Meta:
        ordering = ('-id',)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_image(self,update):
        self.title = update
        self.save()
    
    def __str__(self):
        return self.title
    
    @classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images
    
    @classmethod
    def get_image_by_id(cls, id):
        the_image = Image.objects.get(id =id)
        return the_image
    
    @classmethod
    def filter_by_location(cls, id):
        images = Image.objects.filter(location_id = id)
        return images
    
    @classmethod
    def search_by_category(cls,search_term):
        photo = cls.objects.filter(category__cat_name__icontains=search_term)
        return photo   

