from django.conf.urls import url
from HackNIEC import settings
from . import views
from django.conf.urls.static import static


app_name = 'onlinetest' 
#This sets application namespace to diffretiate urls of different apps.

urlpatterns = [
    #url for home-page:
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    
    #url for login-page:
    url(r'^clientlogin$', views.clientlogin, name='clientlogin'),
    #url for signup-page:
    url(r'^clientregister$', views.clientregister, name='clientregister'),
    url(r'^addidea$', views.addidea, name='addidea'),
    url(r'^submitidea$', views.submitidea, name='submitidea'),
    url(r'^viewidea$', views.viewidea, name='viewidea'),
    url(r'^submitfeedback$', views.submitfeedback, name='submitfeedback'),
    url(r'^feedback$', views.feedback, name='feedback'),
    url(r'^clientadmin$', views.clientadmin, name='clientadmin'),
    url(r'^clientloginval$', views.clientloginval, name='clientloginval'),
    url(r'^clientlogout', views.clientlogout, name='clientlogout'),
    url(r'^register$',views.register, name='register'),
    url(r'^studentmarksdisplay$',views.studentmarksdisplay, name='studentmarksdisplay'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
