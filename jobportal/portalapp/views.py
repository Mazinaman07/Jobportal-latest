from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView

# from django.urls import reverse_lazy
# from .forms import SigninForm
#-------------------------------------

# from .forms import user_form
# from .models import user_model

from django.http import HttpResponse 
from . forms import *
from . models import *

# ------------------------------------

from jobportal.settings import EMAIL_HOST_USER 
from django.contrib import messages
from django.core.mail import send_mail

from django.conf import settings
from django.contrib.auth import authenticate
import uuid

from django.contrib.auth.models import User

# Create your views here.

# main home page

def home(request):
    return render(request,'index.html')

# registration page
#job seaker

def reg(request):
    if request.method == 'POST':
        u = regform(request.POST)
        if u.is_valid():
            unm = u.cleaned_data['username']
            eml = u.cleaned_data['email']
            mb = u.cleaned_data['number']
            db = u.cleaned_data['date']
            qn = u.cleaned_data['education']
            pw = u.cleaned_data['password']
            pwc = u.cleaned_data['cpassword']

            if pw == pwc:
                mod = usermodel(username=unm,email=eml,mob=mb,dob=db,qualification=qn,password=pw)
                mod.save()
                return HttpResponse('successfully registered')
            
            else:
                return HttpResponse('password and cpassword is not match')
        else:
                return HttpResponse('enter valid data')
        
    return render(request,'registration.html')



# login page and userdetail page
# This function validated manually
# all fields fetched from usermodel
#job seaker

def log(request):
     if request.method == 'POST': 
          a = logform(request.POST)
          if a.is_valid():
               em = a.cleaned_data['email']
               pas = a.cleaned_data['password']
               b = usermodel.objects.all() #select * from table name
               
               # itrated i il aahnn variable ullath
               for i in b: 
                    if em == i.email and pas == i.password:
                         unm = i.username
                         id = i.id
                         email = i.email
                         mobile = i.mob
                         dob = i.dob
                         qn = i.qualification

                         context = {
                         'unm': unm,
                         'id': id,
                         'email': email,
                         'mobile': mobile,
                         'dob': dob,
                         'qn': qn,
                        }                          
                         return render(request,'user_detail.html',context)
               else:
                         return HttpResponse('email and password incorrect...')
          else:
                         return HttpResponse('enter invalid data...')
     return render(request,'login.html')




# company side
def regis(request):
    if request.method == 'POST':
        uname = request.POST.get ('uname')
        email = request.POST.get ('email')
        pas = request.POST.get ('password')

        if User.objects.filter(username=uname).first(): #built in model in django
            messages.success(request,'username already taken')
            return redirect(regis)
        
        if User.objects.filter(email=email).first():
            messages.success(request,'email already taken')
            return redirect(regis)
        
        user_obj = User(username=uname,email=email)
        user_obj.set_password(pas)
        user_obj.save()

        auth_token = str(uuid.uuid4()) #link il token pass cheyyunnutha
        profile_obj = profile1.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()

        send_mail_regis(email,auth_token)
        

        return redirect(success) #success url
    
    return render(request,'regi.html')


def send_mail_regis(email,token):
    subject = 'your account has been verified'
    message = f'pass the link to verify your account http://127.0.0.1:8000/verify/{token}'

    email_form = EMAIL_HOST_USER #ayakkande email
    recipient = [email]
    send_mail(subject,message,email_form,recipient) #build in function

   
def success(request): # success - build in function in django

    return render(request,'success.html')

# This function is django form
# Django built in model

# company side 

def logi (request):
    global User
    if request.method == 'POST': #HTTP request method in POST user submit the form
        username = request.POST.get('uname')
        pas = request.POST.get('password')

        user_obj =  User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'user not found')
            return redirect(logi)
        
        # Checking user profile verified:
        # variables ithil aah ullath itrated illa def log il illath pole 
        profile_obj = profile1.objects.filter(user =user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'profile not verified check onemore time')
            return redirect(logi)
        
        User = authenticate (username=username,password=pas)

        if User is None:
            messages.success(request,'wrong password or username')
            return redirect(logi)
        
        username = profile_obj. user.username
        email = profile_obj.user.email
        id = profile_obj.id

        context = {
             'username' : username,
             'email' : email,
             'id' : id,
        }
        # return HttpResponse('success')
        return render(request,'emailHome.html',context)
    return render(request,'logi.html')


# company side 
def verify(request,auth_token):
    profile_obj = profile1.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account already verified')
            redirect(log)
        profile_obj.is_verified = True
        profile_obj.save()
        messages.success(request,'your account verified')
        return redirect(logi)
    
    else:
        return redirect(error)
    

def error(request):
    return render(request,'error.html')



# jobseeker
 
def edititem(request,id):
    user = usermodel.objects.get(id=id)
    if request.method == 'POST':
         user.username = request.POST.get('username')
         user.email = request.POST.get('email')
         user.mob = request.POST.get('number')
         user.dob = request.POST.get('date')
         user.qualification = request.POST.get('education')
         user.save()
         return redirect(log)
    return render(request,'edit_profile.html',{'itm':user})


def postjob(request,id):
    com = profile1.objects.get(id=id)
    if request.method == 'POST':
        a = jobform(request.POST)
        if a.is_valid():
            cn = a.cleaned_data['cname']
            ce = a.cleaned_data['cemail']
            ct = a.cleaned_data['ctitle']
            cty = a.cleaned_data['ctype']
            cx = a.cleaned_data['cexp']
            jt = a.cleaned_data['jtype']

            b = Jobmodel(cname=cn,cemail=ce,ctitle=ct,ctype=cty,cexp=cx,jtype=jt) # model il koduthath ivde veranam
            b.save()            
            return render(request, 'success.html')
        else: # datas valid aayillenkil forms il poyi check cheyyanam
            return redirect(error)
    return render(request,'jobvacancy.html',{'com': com}) #'com' second line il entha kodukkunne ath last kodkknm 



def view_jobs(request,id):
     user_id = id
     job = Jobmodel.objects.all() #difference btwn objects.get and objects.all() ?
     cnm =[]
     ceml =[]
     jtitle = []
     wrktype = []
     exp = []
     jtype = []
     idj = []
     for i in job :
          cnm1 = i.cname
          cnm.append(cnm1)

          ceml1 = i.cemail
          ceml.append(ceml1)

          jtitle1 = i.ctitle
          jtitle.append(jtitle1)

          wrktype1 = i.ctype
          wrktype.append(wrktype1)

          exp1 = i.cexp
          exp.append(exp1)

          jtype1 = i.jtype
          jtype.append(jtype1)
          
          idj1 = i.id
          idj.append(idj1)
    
     job_list = zip(cnm,ceml,jtitle,wrktype,exp,jtype,idj)
     return render(request, 'job_list.html', {'jobs':job_list,'user':user_id})



def job_details(request,id1,id2):
     user_id = id2
     job_id = id1
     job = Jobmodel.objects.get(id=id1)
     a = job.cname
     b = job.cemail
     c = job.ctitle
     d = job.ctype
     e = job.cexp
     f = job.jtype

     context = {"a":a,"b":b,"c":c,"d":d, "e":e, "f":f, 'user':user_id,'job':job_id }
     return render (request,'job_detail.html',context)
          
     
def apply(request,id1,id2):
     user = usermodel.objects.get(id=id1)
     job = Jobmodel.objects.get(id=id2)

     name = user.username
     email = user.email
     cname = job.cname
     jtitle = job.ctitle
     context = {'a':cname,'b':jtitle,'c':name,'d':email}
     if request.method == 'POST':
          application = applyjob() #model
          application.cname = request.POST.get('cname')
          application.jtitle =request.POST.get('jtitle')
          application.name = request.POST.get('name')
          application.email = request.POST.get('email')
          application.quali = request.POST.get('quali')
          application.phone = request.POST.get('phone')
          application.uexp = request.POST.get('uexp')
          application.resume = request.POST.get('resume')
          application.save()
          
          return render(request,'apply_success.html')
     return render(request,'apply_job.html',context)

          
     
def view_applicants(request,id):
     com = profile1.objects.get(id=id)
     com_name = com.user.username
     data = applyjob.objects.all()
     job = []
     nam = []
     eml = []
     quali = []
     ph = []
     exp = []
     cv = []
     for i in data:
          if i.cname == com_name:
               
               jtitle1 = i.jtitle
               job.append(jtitle1)

               name1 = i.name
               nam.append(name1)

               email1 = i.email
               eml.append(email1)

               quali1 = i.quali
               quali.append(quali1)

               phone1 = i.phone
               ph.append(phone1)

               uexp1 = i.uexp
               exp.append(uexp1)

               resume1 = i.resume
               cv.append(str (resume1).split('/')[-1])

     applicants = zip(job,nam,eml,quali,ph,exp,cv)
     return render(request,'show_hover.html',{'applicants':applicants})


def view_applications(request,id):
     u = usermodel.objects.get(id=id)
     username = u.username
     data = applyjob.objects.all()
     job = []
     cnam = []
     cv = []
     for i in data:
          if i.name == username:
               jtitle1 = i.jtitle
               job.append(jtitle1)
               cname1 = i.cname
               cnam.append(cname1)
               resume1 = i.resume
               cv.append(str(resume1).split('/')[-1])
     application = zip(job,cnam,cv)
     return render(request,'show_applications.html',{'application':application})


def companies(request):
     us = usermodel.objects.all()
     li = []
     eml = []
     idc = []
     for i in us:
          cname = i.username
          li.append(cname)
          cemail = i.email
          eml.append(cemail)
          cid = i.id
          idc.append(cid)

          #admin position must be 0th position
          li1 = li[0:]
          eml1 = eml[0:]
          idc1 = idc[0:]
          mylist = zip(li1,eml1,idc1)
          return render(request,'reg_list.html',{'user':mylist})


       





