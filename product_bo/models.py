from django.db import models

# Create your models here.
class product(models.Model):
	product_name = models.CharField(max_length=512)
	product_type = models.CharField(max_length=256)
	create_time = models.DateTimeField('date create')
	img_url = models.FileField(upload_to = 'productImg')
