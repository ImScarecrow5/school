from django import forms

class SchoolForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Ваш e-mail'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Сообщение', 'cols': 30, 'rows': 9}), required=True)