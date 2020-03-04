from django import forms 
from .models import Bed

class NameForm(forms.ModelForm):
    class Meta:
        model=Bed
        fields=['kind','current','increment','decrement','final'] 
    