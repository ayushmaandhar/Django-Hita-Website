import imp
from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from .models import SignUpForm
# signUpForm is from forms.py while SignUpForm is from models.py
from .forms import signUpForm
from django.contrib import messages
from hita.settings import TEMPLATES
from .test_2 import replacev
from django.contrib.auth.forms import UserCreationForm    #for every user

from .models import agreementsellform

from django.core.mail import EmailMessage





def home(request):
    template = 'sprofile/home.html'
    ayush = 'sdkfnoksfnsdfoijsodf'
    context = {'data':ayush}
    return render(request, template, context)

def profile(request):
    template = 'sprofile/profile.html'
    context = {}
    return render(request, template, context) 

def contactus(request):
    template = 'sprofile/contactus.html'
    context = {}
    return render(request, template, context) 

def aboutus(request):
    template = 'sprofile/aboutus.html'
    context = {}
    return render(request, template, context) 

def will(request):
    template = 'sprofile/will.html'
    context = {}
    return render(request, template, context) 

def lease(request):
    template = 'sprofile/lease.html'
    context = {}
    return render(request, template, context) 





# def login(request):            no need as {views.auth.viewLoginview.as_view(template_name='sprofile/login.html') is working}
#     template = 'sprofile/login.html'
#     context = {}


#     return render(request, template, context)

# def logout(request):
#     template = 'sprofile/logout.html'

#     if request.method == 'GET':
#         messages.success(request, f'You have been Logged Out.')  
#         return redirect('home') 
#     else:
#         return render(request, template)    


def signup(request):
    template = 'sprofile/signup.html'

    if request.method == 'POST':
        form = signUpForm(request.POST)   #here form is a local variable
 
        if form.is_valid():
            form.save()    
            username = form.cleaned_data.get('username') # error possiblity get unrecognised
            messages.success(request, f'Hiiiii {username} , your account was created successfully.')  
            return redirect('login')     

    else:
        form = signUpForm()                                            
    return render(request, template, {'form': form})          


def sell(request):
    template = 'sprofile/sell.html'

    return render(request, template)

def sellform(request):
    template = 'sprofile/sellform.html'   

    return render(request, template) 


def thankyou(request): #saves to first table in db
    if request.method == 'POST':
        print(request.POST)
        form = SignUpForm(name= request.POST['name'], email= request.POST['email'], password= request.POST['password'])
        form.save()
    template = 'sprofile/thankyou.html'
    context = {}
    return render(request, template, context) 

def thankyouuu(request): #saves to first table in db
    if request.method == 'POST':
        print(request.POST)
        agreementsellform(
            agree_address = request.POST['poa'],
            agree_date = request.POST['doa'],
            seller_name = request.POST['sn'],
            seller_age = request.POST['sage'],
            seller_occ = request.POST['so'],
            seller_address = request.POST['sadd'],
            buyer_name = request.POST['bn'],
            buyer_age = request.POST['bage'],
            buyer_occ = request.POST['bo'],
            buyer_address = request.POST['badd'],
            property_address = request.POST['padd'],
            price = request.POST['total'],
            token_amount = request.POST['token'],
            bal_amount = request.POST['balance'],
            bal_date = request.POST['bdate'],
            extra_variable = request.POST['bdate']
        ).save()    
        replacev(request.POST)
        
    template = 'sprofile/thankyouuu.html'
    context = {}
    return render(request, template, context)     
    