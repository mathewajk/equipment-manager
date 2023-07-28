from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import GroupForm, EquipmentForm

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
    
add_equipment = AddEquipmentView.as_view()
