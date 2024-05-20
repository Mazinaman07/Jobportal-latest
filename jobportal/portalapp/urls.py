
from django.urls import path
from . views import *
from . import views

# from django.views.generic import TemplateView
# from . views import reg, home, log 


urlpatterns = [
    path('register/',reg),
    path('',home),
    path('login/',log),
    # path('home/',home),

    # path('login/',success.html),    
    # path('success/', TemplateView.as_view(template_name='success.html'), name='success_url')    


    path('regis/',regis),
    path('success/',success),
    path('send/',send_mail_regis),
    path('error/',error),
    path('logi/',logi),
    path('verify/<auth_token>',verify),


    path('edititem/<int:id>',edititem),

    path('postjob/<int:id>', postjob),

    path('joblist/<int:id>',view_jobs),   

    path('jobdetails/<int:id1>/<int:id2>',job_details),

    path('apply/<int:id1>/<int:id2>',apply),

    path('applicant/<int:id>',view_applicants),

    path('application/<int:id>',view_applications),

    path('cdis', companies),
]

