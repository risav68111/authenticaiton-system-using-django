from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.method=='POST':
        username= request.POST['username']
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']

        if User.objects.filter(username=username).exists():
            messages.error(request, f"UserName: {username} already exists")
            return redirect("signup")
        
        if User.objects.filter(email= email).exists():
            messages.error(requset, f"Email already exists")
            return redirect("signup")
        if password1!= password2 :
            message.error(request, f"Password not matched")
            return redirect("signup")

        myuser= User.objects.create_user(username, email, password1)
        myuser.first_name= firstname
        myuser.last_name= lastname
        
        myuser.save()
        
        messages.success(request, "Account has been created successfully.")

        return redirect('signin')
        
    return render(request, 'authen/signup.html')
    
def signin(request):
    
    if request.method== 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user= authenticate(username= username, password= password)

        if user is not None:
            firstname= user.first_name
            login(request, user)
            return render(request, 'authen\index.html', {'firstname': firstname})
        else:
            message= f"User with \"{username}\" does not exist"
            messages.error(request, "bad credentials")
            return render(request,'authen/signup.html', {'message': message})

    return render(request, 'authen/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return render('home')