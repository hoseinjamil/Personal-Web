from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={"class": "form-group", 'placeholder': 'Your Name'}))
    email = forms.EmailField()
    subject = forms.CharField(max_length=50,
                              widget=forms.TextInput(attrs={"class": "form-group", 'placeholder': 'Subject'}))
    body = forms.CharField(max_length=500,
                           widget=forms.Textarea(attrs={"class": "form-group", 'placeholder': 'Message'}))
