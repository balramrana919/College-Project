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

class BookDetailModel(models.Model):
    book_id = models.IntegerField(max_length=10)
    bookName = models.CharField(max_length=20)
    bookAuthor = models.CharField(max_length=20)
    bookPublication = models.CharField(max_length=50)
    bookPublishDate = models.DateField()
    bookGenre = models.CharField(max_length=20)

    class Meta:
        db_table = 'bookdetail_db'


