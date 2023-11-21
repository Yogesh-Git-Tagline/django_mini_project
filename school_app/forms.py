from django import forms
from .models import Student


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email_id',
                  'contact_number', 'address', 'photo']

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}), error_messages={'required': 'Please enter your first name'})
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}), error_messages={'required': 'Please enter your last name'})
    email_id = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email id'}), error_messages={'required': 'Please enter your email id'})
    contact_number = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}), max_length=10, error_messages={'required': 'Please enter your contact number'})
    address = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Enter address'}), error_messages={'required': 'Please enter your full address'})
    photo = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control'}), error_messages={'required': 'Please choose image'})
