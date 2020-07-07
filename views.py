from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import User,App,Review,blockwords
from django.contrib.auth.models import User as us

# Create your views here.
def index(request):
    mydict={
        "id":"1001",
        "name":"Athira"
    }
    return render(request,"new.html", context=mydict)
def home(request):
    mydict={
        "id":"1001",
        "name":"Athira",
        "course":"MCA"
    }
    return render(request,"student.html", context=mydict)
def reg(request):
    return render(request,"reg.html")
def temp(request):
    return render(request,"template.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def forgot_pswd(request):
    return render(request,"forgot_pswd.html")
def postData(request):
    a=request.POST.get('appname')
    my_dict={
        'A':a,
        'data':""
        } 
    if request.method=="POST":
        AlData=App()
        AlData.appname=request.POST.get('appname')
        AlData.description=request.POST.get('description')
        AlData.developer=request.POST.get('developer')
        AlData.size="Size"
        AlData.save()
    
    return HttpResponse(a)

def loadData(request):
    AlData=App.objects.all()
    my_dict={
        'data':AlData
    }
    return render(request,'app.html',context=my_dict)

def user_chk(request):
    if request.method=="POST":
        userData=User.objects.filter(username=request.POST.get('username'),password=request.POST.get('pass'))
        print(request.POST.get('username'))
        print(userData.count())

        if userData.count()>0:
            for us in userData:
                request.session["sid"]=us.id
                print(us.id)
                return loadData(request)
        else:
            my_dict={
            'A':"Wrong Password", 
            'data':""
             } 
    return render (request,"login.html")

def reviewApp(request):
    
    AlData=App.objects.filter(pk=request.GET["id"])
    my_dict={
        'data':AlData
    }
    return render (request,"reviewapp.html",context=my_dict)

def sendreview(request):
    if request.method=="POST":
        msg=Review()
        msg.appname=get_object_or_404(App, pk=request.POST.get("appName"))
        msg.username=get_object_or_404(User, pk=request.session["sid"])
        msg.review=request.POST.get("review")
        data=request.POST.get("review").split()
        counter=0
        words=0
        for dt in data:
            bw=blockwords.objects.filter(blockwords=dt)
            words=words+1
            if bw.count()>0:
                counter=counter + 1

        
        if counter>=0:
            print((counter/words)/100)
            msg.rating=(counter/words)*100

        

        msg.save()
    return loadData(request)


def seereview(request):
    AlData=Review.objects.filter(appname=get_object_or_404(App, pk=request.GET["id"]))
    my_dict={
        'data':AlData
    }
    return render (request,"seereviews.html",context=my_dict)


def saveUser(request):
	if request.method=="POST":
		ur=User()
		ur.name=request.POST.get('name')
		ur.username=request.POST.get('username')
		ur.email=request.POST.get('email')
		ur.password=request.POST.get('password')
		ur.save()
	return render(request,"login.html")

def Ownerreg(request):
	if request.method=="POST":
		ur=us.objects.create_user(request.POST.get('username'),request.POST.get('email'), request.POST.get('password'))
		
		ur.save()
	return render(request,"ownerregister.html")

def Ownerregister(request):
	return render(request,"ownerregister.html")


    