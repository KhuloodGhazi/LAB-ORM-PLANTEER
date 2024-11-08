from django.urls import path
from . import views


app_name = "plants"

urlpatterns = [
    path("all/", views.all_plants_view, name="all_plants_view"),
    path("new/", views.new_plants_view, name="new_plants_view"),
    path("detail/<plant_id>", views.plant_detail_view, name="plant_detail_view"),
    path("update/<plant_id>", views.plant_update_view, name="plant_update_view"),
    path("delete/<plant_id>", views.plant_delete_view, name="plant_delete_view"),
    path("search/", views.search_plant_view, name="search_plant_view"),
]