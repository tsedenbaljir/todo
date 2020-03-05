from django.core.exceptions import NON_FIELD_ERRORS
from django import forms 
from .models import Bed

class NameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(NameForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['kind'].required = False
        self.fields['current'].required = False
        self.fields['increment'].required = False
        self.fields['decrement'].required = False
        self.fields['final'].required = False
        self.fields['current'].invaled = "asdfsadfasd"

    class Meta:
        model=Bed
        fields=['kind','current','increment','decrement','final'] 
        labels = {
            "kind": "Орны төрөл (байнгын болон яаралтай тусламж, үйлчилгээний)",
            "current": "Одоогийн тусгай зөвшөөрөлтэй ор",
            "increment": "Шинээр санал болгож буй ор",
            "decrement": "Санал болгож буй орны бууралт",
            "final": "Төсөл дууссаны дараах нийт ор",
        }
        error_messages={'invalid': 'your custom error message'}
 