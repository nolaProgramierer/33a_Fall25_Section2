from django import forms


class AddPianoForm(forms.Form):
    brand = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Piano brand",
    })
    )
    finish = forms.CharField(
         widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Piano finish"
    })
    )
    price = forms.IntegerField(
         widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Piano price"
    })
    )