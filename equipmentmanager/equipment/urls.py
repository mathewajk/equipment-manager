from django.urls import path
from . import views

app_name = "equipment"
urlpatterns = [
    path(route='group/add',
         view=views.add_group,
         name='add-group'),
    path(route='equipment/add',
         view=views.add_equipment,
         name='add-equipment'),
    path(route='equipment/list',
         view=views.list_equipment,
         name='list-equipment')
]