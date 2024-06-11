from django.shortcuts import render,redirect
from AdminApp.models import AllCategories ,NewArrivals
from UserApp.models import UserInfo,MyCart

# Create your views here.
def home(request):
    sach = AllCategories.objects.all()
    drush = NewArrivals.objects.all()
    return render(request,"master.html",{"sach":sach,"drush":drush})
def showNew(request,id):
    sach = AllCategories.objects.all()
    drush = NewArrivals.objects.filter(category=id)
    return render(request,"master.html",{"drush":drush,"sach":sach})
def ViewDetails(request,id):
    sach = AllCategories.objects.all()
    arrival = NewArrivals.objects.get(id=id)
    return render(request,"ViewDetails.html",{"arrival": arrival,"sach":sach})
def Login(request):
    if(request.method=="GET"):
        return render(request,"Login.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            user = UserInfo.objects.get(user=uname,password=pwd)            
        except: 
            message = "Invalid Credentials,Plz try again!!"
            return render(request,"Login.html",{"message":message})
        else:  
           
            request.session["uname"] = uname
            return redirect(home)
        
def BookForME(request): 
    if("uname" in request.session):
        user = UserInfo.objects.get(user_name = request.session["uname"])
        NewArrivals_id = request.POST["pid"]
        arrival = NewArrivals.objects.get( id=NewArrivals_id )
        qty = request.POST["qty"]
        cart = BookForME()
        cart.user = user
        cart.qty = qty
        cart.save() 
        return redirect(home)
    else:
        return redirect(Login)

def SignOut(request):
    #delete the session
    request.session.clear()
    return redirect(home)
def SignUp(request):
    if(request.method=="GET"):
        return render(request,"SignUp.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            user = UserInfo.objects.get(user_name=uname)            
        except:
            user = UserInfo(uname,pwd)
            user.save()
            return redirect(home)
        else:
            message = "This user already exist"
            return render(request,"SignUp.html",{"message":message})
       