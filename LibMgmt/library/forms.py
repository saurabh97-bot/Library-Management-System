from django import forms
from .models import *
from django.contrib.auth.models import User


class Addbook(forms.ModelForm):
    class Meta:
        model = BookDataset
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),

        }


class DateInput(forms.DateInput):
    input_type = 'date'


class Issuebook(forms.ModelForm):
    class Meta:
        model = IssueRecords
        fields = '__all__'

        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'book_id': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'issue_date': DateInput(attrs={'type': 'date'})

        }

class DateInput(forms.DateInput):
    input_type = 'date1'

class StudentData(forms.ModelForm):
    class Meta:
        model = StudentRecords
        fields = '__all__'

        widgets = {

            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'return_date': DateInput(attrs={'type': 'date1'}),
            'issue_date': DateInput(attrs={'type':'date1'})

        }


class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'password']


