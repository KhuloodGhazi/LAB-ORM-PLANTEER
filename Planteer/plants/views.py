from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Plant
from django.core.paginator import Paginator




# Create your views here.

def all_plants_view(request:HttpRequest):

    plant = Plant.objects.all()

    return render(request, 'plants/all_plants.html', {"plant":plant})




def new_plants_view(request:HttpRequest):

    if request.method == "POST":
        new_plant = Plant(
            name=request.POST["name"],
            about=request.POST["about"],
            used_for=request.POST["used_for"],
            image=request.FILES["image"],
            native_locations=request.POST["native_locations"],
            category=request.POST["category"],
            is_edible=request.POST.get("is_edible") == "True"
            )

        new_plant.save()

        #return redirect("plants:plant_published_view")


    return render(request, 'plants/add_new_plants.html')




def plant_detail_view(request:HttpRequest, plant_id:int):

    plant = get_object_or_404(Plant, pk=plant_id)
    
    related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant_id)[:3]  
    
    return render(request, 'plants/plant_detail.html', {
        "plant": plant,
        "related_plants": related_plants
    })




def plant_update_view(request:HttpRequest, plant_id:int):

    plant = Plant.objects.get(pk=plant_id)
    
    if request.method == "POST":
        plant.name=request.POST["name"],
        plant.about=request.POST["about"],
        plant.used_for=request.POST["used_for"],
        if "plants_image" in request.FILES: plant.image=request.FILES["image"],
        plant.native_locations=request.POST["native_locations"],
        plant.category=request.POST["category"],
        plant.is_edible=request.POST.get("is_edible") == "True"

        plant.save()

        return redirect("plants:plant_updated_view", plant_id=plant.id )

    return render(request, 'plants/plant_update.html', {"plant":plant})




def plant_delete_view(request:HttpRequest, plant_id:int):

    plant = Plant.objects.get(pk=plant_id)
    plant.delete()

    return redirect("main:main_view")

    #return render(request, 'plants/plant_delete.html')




def search_plant_view(request:HttpRequest):

    if "search" in request.GET and len(request.GET["search"]) >= 3:
        plant = Plant.objects.filter(name__ontains=request.GET["search"])

    else:
        plant = []    

    return render(request, 'plants/search_plant.html', {"plant":plant})