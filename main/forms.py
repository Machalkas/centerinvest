from django import forms
from .models import Queue

class BranchForm(forms.ModelForm):

    class Meta:
        model=Queue
        fields=[]
        