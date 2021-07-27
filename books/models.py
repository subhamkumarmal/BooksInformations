from django.db import models

# Create your models here.
class BooksDetails(models.Model):
    book_id=models.AutoField
    book_name=models.CharField(max_length=30,default="")
    book_writer=models.CharField(max_length=20,default="")
    book_price=models.IntegerField(default=0)
    book_discount=models.IntegerField(default=0)
    book_imgs=models.ImageField(upload_to='books/images',default="")

    def __str__(self):
        return self.book_name


