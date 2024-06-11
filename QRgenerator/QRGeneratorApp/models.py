from django.db import models

# Create your models here.
class FilesCollect(models.Model):
    url_text=models.CharField(max_length=256)
    img_upload=models.ImageField(upload_to='images/%y')

#    showing the url instead of object in admin portal
    def __str__(self):
         return self.url_text
