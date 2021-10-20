from django.forms import ModelForm
from .models import *
class ApplyForm(ModelForm):
    class Meta:
        model=Job
        fields="__all__"