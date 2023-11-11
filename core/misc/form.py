from django import forms

class postcardForm(forms.Form):
    title = forms.CharField(max_length = 64)
    description = forms.CharField(max_length = 256)
    to = forms.EmailField(max_length = 32)
