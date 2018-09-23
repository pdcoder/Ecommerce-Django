from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your full name"
            }
        )
    )
    email = forms.EmailField(
         widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your mail"
            }
        )
    )
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your message"
            }
        )
    )