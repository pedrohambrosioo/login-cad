from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from setup import settings
from django.core.mail import send_mail


def home(request):
    return render(request, 'authentication/index.html')

def signup(request):

    if request.method == 'POST':
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, 'Username already exist! please try some other username !')
            return redirect('signup')

        #if User.objects.filter(email=email):
            #messages.error(request, 'Email already registered !')
            #return redirect('signup')

        if len(username)>10:
             messages.error(request, 'Username must be under 10 characters !')
            
        if pass1 != pass2:
            messages.error(request, 'Password didnt match !')
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, 'Username must be Alpha-numeric !')
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.firt_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'your account has been sucessfully created. ')


        #email
        subject = 'Welcome Django login'
        message = 'Hello' + myuser.first_name + '!! \n' + 'welcome to site \n Thank your visiting our website\n we have also sent you a confirm email, please confirm  your email addres in order to activate your account \n\n Thanking you ' 
        from_email = settings.EMAIL_HOST_USER 
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)


        return redirect('signin')
    return render(request, 'authentication/signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'authentication/index.html', {'fname': fname})
        else:
            messages.error(request, 'Bad credentials')
            return redirect('signin')
        
    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged out Sucessfully")
    return redirect('home')
