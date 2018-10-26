from django.forms import ModelForm
from .models import Lost, Found


class LostForm(ModelForm):
    class Meta:
        model = Lost
        fields = ['name', 'address', 'pic']


class FoundForm(ModelForm):
    class Meta:
        model = Found
        fields = ['name', 'address', 'pic', 'location']
