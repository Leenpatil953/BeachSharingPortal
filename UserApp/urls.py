from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('showNew/<id>',views.showNew),
    path('ViewDetails/<id>',views.ViewDetails),
    path('SignUp',views.SignUp),
    path('Login',views.Login),
    path('SignOut',views.SignOut),
    path('BookForME',views.BookForME),
    ]
