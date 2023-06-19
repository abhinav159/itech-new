from django.contrib import admin
from .models import Contact,Student_details,Cards,User_details, Course_details

                                          
class Useredit(admin.ModelAdmin):               
    search_fields = ['first_name']
    list_display = ['name','phone','course','address_1']
    list_filter=('course','name','referal') 

admin.site.register(Student_details, Useredit)
admin.site.register(Contact)
admin.site.register(Cards)
admin.site.register(User_details)
admin.site.register(Course_details)

