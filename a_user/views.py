from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


def home(request):
    return render(request, 'a_user/home.html')

def registeruser(request):
    if request.method=='GET':
        return render(request, 'a_user/registeruser.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        password1 = request.POST['pass1']
        if User.objects.filter(username=username).exists():
            return render(request, 'a_user/registeruser.html',{'error':'username or email has been taken. choose another'})

        elif User.objects.filter(email=email).exists():
            return render(request, 'a_user/registeruser.html',{'error':'username or email has been taken. choose another'})

        elif password == password1:
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save();
            auth.login(request, user)
            return redirect('welcome')
        else:
            return render(request, 'a_user/registeruser.html',{'error':'Password didnt match'})



def signupuser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('welcome')
        else:
            return render(request, 'a_user/signupuser.html', {'error': 'Invalid Username or password'})

    else:
        return render(request, 'a_user/signupuser.html')

def logoutuser(request):
    if request.method=='POST':
        auth.logout(request)
        return render(request, 'a_user/home.html',{'error':'details has been stored thankyou'})
    else:
        return render(request, 'a_user/welcome.html')

def thankyou(request):
    return render(request, 'a_user/thankyou.html')

def welcome(request):
    return render(request, 'a_user/welcome.html')
