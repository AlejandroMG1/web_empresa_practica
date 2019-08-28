from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'pon tu nombre'}
    ))
    email = forms.EmailField(label="E-Mail", required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'pon tu email'}
    ))
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'pon tu mensaje'}
    ))
