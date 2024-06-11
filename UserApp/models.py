from django.db import models
from AdminApp.models import NewArrivals


class UserInfo (models.Model):
   user_name = models.CharField(max_length=20,primary_key=True)
   password = models.CharField(max_length=20)

   class Meta:
      db_table="UserInfo"

class MyCart(models.Model):
   user = models.ForeignKey(UserInfo,on_delete = models.CASCADE)
   Available = models.IntegerField(default=1)

   class Meta:
      db_table="MyCart"
