from django.db import models
class real(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	message=models.CharField(max_length=200)
	# class  Meta:
	# 	db_table="BK_real"
	
# Create your models here.
