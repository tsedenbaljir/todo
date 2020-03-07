from django import forms 
from .models import *

class NameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)
        for k,f in self.fields.items():
            if 'invalid' in f.error_messages:
                self.fields[k].error_messages['invalid'] = 'Буруу формат байна.'
            if 'required' in f.error_messages:
                self.fields[k].error_messages['required'] = 'Бөглөх шаардлагатай.'
            if 'max_length' in f.error_messages:
                self.fields[k].error_messages['max_length'] = 'Хэт урт байна.'
            if 'min_length' in f.error_messages:
                self.fields[k].error_messages['min_length'] = 'Хэт богино байна.'
        
        for key, field in self.fields.items():
            print(field.widget)
            if isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'placeholder': "songolt xiine vv"})
            if isinstance(field.widget, forms.NumberInput):
                field.widget.attrs.update({'placeholder': "Зөвхөн тоо "})
        
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