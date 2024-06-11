from django.db import models


class AllCategories (models.Model):
    Category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.Category_name
    
    class Meta:
        db_table="AllCategories"
    

class NewArrivals (models.Model):
   name = models.CharField(max_length=200)
   Code = models.CharField(max_length=20)
   Description = models.CharField(max_length=200)
   images = models.ImageField(upload_to="images",default="abc.jpg")
   category= models.ForeignKey(AllCategories,on_delete = models.CASCADE)

   class Meta:
      db_table="NewArrivals"