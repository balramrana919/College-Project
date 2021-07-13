from django.db import models




# Create your models here.
class libraryuserModel(models.Model):
    L_ID = models.CharField(max_length=10)
    fullname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField()

    class Meta:
        db_table = 'libraryuser_db'