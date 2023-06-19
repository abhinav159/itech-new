from django.shortcuts import render, redirect
from .models import Student_details, Contact,Cards,User_details, Course_details
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import auth, User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
    course_card = Course_details.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        number = request.POST.get('phone')

        user = User_details(email = email, username= name, phone = number)
        user.save()
    return render(request,'index.html',{'course_card':course_card})

def aboutus(request):
    return render(request,'aboutus.html')

def box(request):
    return render(request,'box.html')

def course(request):
    card_element=Cards.objects.all() 


    return render(request,'course.html',{'card_element':card_element})

def service(request):
    return render(request,'service.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        message = request.POST.get('message')
        contact = Contact(name = name, email = email, telephone = telephone, message = message)
        contact.save()

    return render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')

def registration_email(request):
    return render(request,'registration_email.html')



def registration(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        select = request.POST.get('select')
        qualification = request.POST.get('qualification')
        parent_number = request.POST.get('parent_number')
        postal = request.POST.get('postal')

        # message = "This is a conformation message from itech academy"
         
        # send_mail(
        #     'message',
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [email,],
        #     fail_silently=False

        # )
        

        student = Student_details(name = full_name, email = email, phone = phone_number, date = dob, gender = gender, address_1 = address1,
                                  address_2 = address2, course = select, qualification = qualification, parent_number = parent_number,
                                   postal = postal)
        mydict = {'username': full_name}
        student.save()
        html_template = 'registration_email.html'
        html_message = render_to_string(html_template, context=mydict)
        subject = 'Welcome to Itech Academy'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
        message.content_subtype = 'html'
        message.send()

    return render(request,'registration.html' )