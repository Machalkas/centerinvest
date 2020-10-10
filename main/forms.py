from django import forms
from .models import Queue, Services, Branch

class QueueForm(forms.ModelForm):
    time=forms.CharField()
    service=forms.ModelChoiceField(queryset=Services.objects.all())
    branch=forms.ModelChoiceField(queryset=Branch.objects.all())
    number=forms.CharField(empty_value="-")
    class Meta:
        model=Queue
        fields=['time', 'service', 'branch', 'number']
        