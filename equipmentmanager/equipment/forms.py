from django import forms
from django.contrib.auth import get_user_model

from .models import Group, Equipment, Performance

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ["name"]
        labels = {
            'name': 'Group name'
        }

class EquipmentForm(forms.ModelForm):

    instrument_type = forms.ChoiceField(choices=Equipment.INSTRUMENT_CHOICES)
    size = forms.ChoiceField(choices=Equipment.SIZE_CHOICES)

    class Meta:
        model = Equipment
        fields = ["instrument_type", "size", "number", "stand", "number", "owner", "location"]
        labels = {
            'instrument_type': 'Drum'
        }

    def owner_queryset(self):
        return get_user_model().objects.all()