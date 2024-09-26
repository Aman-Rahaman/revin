from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm
from .models import User_table, UserProfile_table
# Create your views here.


def user_table(request):
    table = {'table': User_table.objects.all()}
    return render(request, "admin_dashboard/user_table.html", table)


# def user_form(request, id=0):
#     if request.method == "GET":
#         if id==0:
#             form = UserForm()
#             # form_p = UserProfileForm()
#         else:
#             user_entry = User_table.objects.get(pk=id)
#             form = UserForm(instance=user_entry)
#             # userprofile_entry = UserProfile_table.objects.get(user_id=id)
#             # form_p = UserProfileForm(instance=user_entry)
#         return render(request, "admin_dashboard/user_form.html", {'form':form})
#     else:
#         if id==0:
#             form = UserForm(request.POST)
#         else:
#             user_entry = User_table.objects.get(pk=id)
#             form = UserForm(request.POST, instance=user_entry)
#         if form.is_valid():
#             form.save()
#         return redirect("/user/table2/")



def user_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = UserForm()
            form_p = UserProfileForm()
        else:
            user_entry = User_table.objects.get(pk=id)
            form = UserForm(instance=user_entry)
            userprofile_entry = UserProfile_table.objects.get(user_id=id)
            form_p = UserProfileForm(instance=userprofile_entry)
        return render(request, "admin_dashboard/user_form.html", {'form':form, 'form_p':form_p})
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_address = request.POST.get('email_address')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')
        full_name = first_name + " " + last_name
        
        if id != 0:
            user_entry = User_table.objects.get(pk=id)
            user_entry.delete()

        User_table(first_name=first_name, last_name=last_name, email_address=email_address, password=password).save()
        user_entry = User_table.objects.get(email_address=email_address)
        UserProfile_table(name=full_name, email=email_address, user_id=user_entry, phone_number=phone_number).save()

        return redirect("/user/table/")
        


def user_delete(request, id=-1):
    if request.method == "POST":
        user_entry = User_table.objects.get(pk=id)
        user_entry.delete()
        return redirect("/user/table/")



def user_table2(request):
    table = {'table': User_table.objects.all()}
    return render(request, "admin_dashboard/new_user_table.html", table)

def user_form2(request, id=0):
    return render(request, "admin_dashboard/new_user_form.html")

def userprofile_table(request, id=0):
    table = {'table': UserProfile_table.objects.all()}
    return render(request, "admin_dashboard/new_userprofile_table.html", table)