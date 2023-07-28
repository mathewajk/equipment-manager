from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .forms import GroupForm, EquipmentForm
from .models import Equipment

class AddGroupView(TemplateView):

    form = GroupForm
    template_name = "pages/add-group.html"

    def get(self, request, *args, **kwargs):
        self.obj_form = self.form()
        return self.render_to_response(self.get_context_data(**kwargs))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.obj_form
        return context
    
add_group = AddGroupView.as_view()

class AddEquipmentView(TemplateView):

    form = EquipmentForm
    template_name = "pages/add-group.html"

    def get(self, request, *args, **kwargs):
        self.obj_form = self.form()
        return self.render_to_response(self.get_context_data(**kwargs))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.obj_form
        return context

    def post(self, request, *args, **kwargs):
        self.obj_form = self.form(data=request.POST)
        if self.obj_form.is_valid():
            self.obj_form.save()
        return self.render_to_response(self.get_context_data(**kwargs))
    
add_equipment = AddEquipmentView.as_view()


class EquipmentListView(ListView):

    model = Equipment
    template_name = "pages/list-equipment.html"

list_equipment = EquipmentListView.as_view()
