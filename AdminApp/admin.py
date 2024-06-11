from django.contrib import admin
from .models import NewArrivals ,AllCategories


class AllCategoriesAdmin(admin.ModelAdmin):
    list_display=("id","Category_name")

class NewArrivalsAdmin(admin.ModelAdmin):
    list_display=("id","name","Code","Description","images","category")


admin.site.register(AllCategories ,AllCategoriesAdmin )
admin.site.register(NewArrivals ,NewArrivalsAdmin)

