from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Plant



# Create your views here.

def all_plants_view(request:HttpRequest):

    return render(request, 'plants/all_plants.html')




def new_plants_view(request:HttpRequest):

    if request.method == "POST":
        new_plant = Plant(
            name=request.POST["name"],
            about=request.POST["about"],
            used_for=request.POST["used_for"],
            image=request.FILES["image"],
            native_locations=request.POST["native_locations"],
            category=request.POST["category"]
        )

        new_plant.save()

        #return redirect("plants:plant_published_view")


    return render(request, 'plants/add_new_plants.html')




def plant_detail_view(request:HttpRequest):

    return render(request, 'plants/plant_detail.html')




def plant_update_view(request:HttpRequest):

    return render(request, 'plants/plant_update.html')




def plant_delete_view(request:HttpRequest):

    return render(request, 'plants/plant_delete.html')




def search_plant_view(request:HttpRequest):

    return render(request, 'plants/search_plant.html')