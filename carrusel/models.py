from django.db import models
img_path = 'static\carrusel'
class HomeSlide(models.Model):
    image = models.ImageField(upload_to=f'{img_path}')

    def __str__(self):
        return self.image.name