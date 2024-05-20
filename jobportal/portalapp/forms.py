from django import forms
from . models import *




class regform(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    number = forms.IntegerField()
    date = forms.DateField()
    education = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    cpassword = forms.CharField(max_length=100)


class logform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)




# class JobForm(forms.ModelForm):
#     class Meta:
#         model = Jobmodel
#         fields = '__all__'



class jobform(forms.Form):
    cname = forms.CharField(max_length=100)
    cemail = forms.EmailField()
    ctitle = forms.CharField(max_length=100)
    ctype = forms.CharField(max_length=100)
    cexp =forms.CharField(max_length=100)
    jtype = forms.CharField(max_length=100)



# class Jobform(forms.ModelForm):
#     class Meta:
#         model = Job
#         fields = ['company_name', 'email', 'job_title', 'work_type', 'experience', 'job_type']
     




# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields= ['username','email','mobile','dob','education','password1','password2']


# class SigninForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields= ['email','password1']  


# class user_form(forms.Form):
#     username = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     mob = forms.IntegerField()
#     dob = forms.DateField()
#     qualification = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=100)
#     cpassword = forms.CharField(max_length=100)


   