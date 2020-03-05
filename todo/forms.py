from django import forms 
from .models import Bed

class NameForm(forms.ModelForm):

    def __init__( self, *args, **kwargs ):
        super(NameForm, self).__init__( *args, **kwargs )
        self.fields['kind'].label = False #the trick :)

    class Meta:
        model=Bed
        fields=['kind']  
        # fields=['kind','current','increment','decrement','final'] 
    