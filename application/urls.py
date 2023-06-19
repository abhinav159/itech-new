from django.urls import path
from itechacademy.settings import DEBUG,STATIC_URL,STATIC_ROOT,MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from django.contrib import admin
from . import views
app_name = 'common'
urlpatterns = [
    # path('',views.base,name='base'),
    path('',views.index,name='index'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('course',views.course,name='course'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('box',views.box,name='box'),
   
    path('registration',views.registration,name='registration'),
    path('registration_email',views.registration_email,name='registration_email'),
]
if DEBUG:
    urlpatterns += static(STATIC_URL,document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)