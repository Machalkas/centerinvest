from django import forms
from .models import Queue, Services, Branch
from django.utils import timezone

class QueueForm(forms.ModelForm):
    time=forms.DateTimeField(input_formats=['%H:%M %d.%m.%Y'], initial=timezone.now)
    service=forms.ModelChoiceField(queryset=Services.objects.all())
    branch=forms.ModelChoiceField(queryset=Branch.objects.all())
    number=forms.CharField(empty_value="-")
    class Meta:
        model=Queue
        fields=['time', 'service', 'branch', 'number']
        