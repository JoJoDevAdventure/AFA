from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}'
    

class Product (models. Model):
    collection = models.ForeignKey (Collection, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models. DecimalField (max_digits=6, decimal_places=2)
    image = models. ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models. ImageField (upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.collection.slug}/{self.slug}'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self. image.url
        return ''
    
    def get_thumbnaiil(self):
        if self.thumbnail :
            return 'http://127.0.0.1:8000' + self. thumbnail.url
        else :
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self. thumbnail.url
            else :
                return ''
    
    def make_thumbnail(self, image, size=(300,300)):
        img = Image. open (image)
        img. convert ('RGB')
        img. thumbnail (size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumb = File(thumb_io, name=image.name)

        return thumb