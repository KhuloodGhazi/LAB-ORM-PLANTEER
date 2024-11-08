from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Contact
from plants.models import Plant



# Create your views here.

def main_view(request:HttpRequest):

    plant = Plant.objects.all().order_by("-create_at")[0:3]

    return render(request, 'main/home.html', {"plant":plant})





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