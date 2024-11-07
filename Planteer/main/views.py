from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Contact


# Create your views here.

def main_view(request:HttpRequest):

    return render(request, 'main/home.html')




def contact_view(request:HttpRequest):

    if request.method == "POST":
        new_message = Contact(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            message=request.POST["message"]
            )
        
        new_message.save()

        return redirect("main:message_view")


    return render(request, 'main/contact.html')




def message_view(request:HttpRequest):

    messages = Contact.objects.all()

    return render(request, 'main/message.html', {"messages":messages})