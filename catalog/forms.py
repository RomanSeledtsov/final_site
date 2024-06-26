from django import forms
from . import models


class InvForm(forms.ModelForm):
    class Meta:
        model = models.Inventory
        fields = "__all__"
