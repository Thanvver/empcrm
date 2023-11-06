from django import forms

from crm.models import Employees

class EmployeeForm(forms.Form):

    name=forms.CharField()
    department=forms.CharField()
    salary=forms.IntegerField()
    email=forms.EmailField()
    age=forms.IntegerField()
    contact=forms.CharField()

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields="__all__"
