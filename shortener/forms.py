from django import forms
from .validators import validate_url

class SubmitUrlForm(forms.Form):
    ''' URL form for DirURL '''
    url = forms.CharField(  label = "Submit URL", 
                            required=True , 
                            validators = [validate_url], 
                            widget=forms.TextInput(attrs = {'placeholder': 'place your url'})
        )