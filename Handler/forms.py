from django import forms

class ID_Form(forms.Form):
    ID = forms.IntegerField(widget = forms.NumberInput(attrs = {
        'placeholder': 'ID',
    }))