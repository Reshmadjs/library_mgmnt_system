from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect,redirect)
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login



from .forms import BooksForm
from .models import Book
def index(request):
    return render(request,"libraryapp/index.html")
    
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        fname=request.POST['fname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']


        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('signin')   



    return render(request,"libraryapp/signup.html")

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']

        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"libraryapp/index.html",{'fname':fname})

        else:
            messages.error(request,"wrong credentials!")
            return redirect("index")
            
    return render(request,"libraryapp/signin.html")


def create_view(request):
    context={}
    form=BooksForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request,"libraryapp/create_view.html",context) 


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Book.objects.all()
         
    return render(request, "libraryapp/list_view.html", context) 


# pass id attribute from urls

def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = Book.objects.get(id = id)
         
    return render(request, "libraryapp/detail_view.html", context)   


 # after updating it will redirect to detail_View
# def detail_view(request, id):
#     # dictionary for initial data with
#     # field names as keys
#     context ={}
  
#     # add the dictionary during initialization
#     context["data"] = Book.objects.get(id = id)
          
#     return render(request, "libraryapp/detail_view.html", context)
 
# update view for details

def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Book, id = id)
 
    # pass the object as instance in form
    form = BooksForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("../list/all")
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "libraryapp/update_view.html", context)
    

 # delete view for details

def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Book, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/libraryapp/list/all")
 
    return render(request, "libraryapp/delete_view.html", context)      