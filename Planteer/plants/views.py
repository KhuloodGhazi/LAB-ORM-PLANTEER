from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Plant
from django.core.paginator import Paginator




# Create your views here.

def all_plants_view(request:HttpRequest):
    
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    is_edible_filter = request.GET.get('is_edible', '')
    
    plants = Plant.objects.all()

    if search_query:
        plants = plants.filter(name__icontains=search_query)

    if category_filter:
        plants = plants.filter(category=category_filter)

    if is_edible_filter:
        plants = plants.filter(is_edible=(is_edible_filter == 'True'))

    paginator = Paginator(plants, 9)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
        
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'category_filter': category_filter,
        'is_edible_filter': is_edible_filter,
        
    }

    return render(request, 'plants/all_plants.html', context)




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

        return redirect("plants:plant_added_view")


    return render(request, 'plants/add_new_plants.html')




def plant_detail_view(request:HttpRequest, plant_id:int):

    try:
        plant = Plant.objects.get(pk=plant_id)
        
        related_plants = Plant.objects.filter(category=plant.category).exclude(id=plant_id)[:3]  
        
        return render(request, 'plants/plant_detail.html', {
            "plant": plant,
            "related_plants": related_plants
            })
    
    except Plant.DoesNotExist:
        return render(request, "plants/page_not_found.html", status=404)




def plant_update_view(request: HttpRequest, plant_id: int):
    plant = get_object_or_404(Plant, pk=plant_id)
    
    if request.method == "POST":
        plant.name = request.POST.get("name", plant.name)
        plant.about = request.POST.get("about", plant.about)
        plant.used_for = request.POST.get("used_for", plant.used_for)
        plant.native_locations = request.POST.get("native_locations", plant.native_locations)
        plant.category = request.POST.get("category", plant.category)
        plant.is_edible = request.POST.get("is_edible") == "True"

        if request.FILES.get("image"):
            plant.image = request.FILES["image"]

        plant.save()

        return redirect("plants:plant_updated_view", plant_id=plant.id)

    return render(request, 'plants/plant_update.html', {"plant":plant})




def plant_delete_view(request:HttpRequest, plant_id:int):

    plant = Plant.objects.get(pk=plant_id)
    plant.delete()

    return redirect("plants:plant_deleted_view")

    #return render(request, 'plants/plant_delete.html')




def search_plant_view(request: HttpRequest):

    search_query = request.GET.get("search", "")

    if search_query and len(search_query) >= 3:
        plants = Plant.objects.filter(name__icontains=search_query)
    else:
        plants = []

    return render(request, 'plants/search_plant.html', {"plant": plants, "search_query": search_query})




def plant_updated_view(request:HttpRequest, plant_id:int):

    plant = Plant.objects.get(pk=plant_id)

    
    return render(request, 'plants/plant_updated.html', {"plant":plant})




def plant_deleted_view(request:HttpRequest):
    
    return render(request, 'plants/plant_deleted.html')




def plant_added_view(request:HttpRequest):

    return render(request, 'plants/plant_added.html')