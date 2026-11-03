from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = ('employee_id','employee_name',..)
        fields = '__all__'

    def clean_employee_email(self):
        return self.cleaned_data['employee_email'].strip().lower()  # Convert email to lowercase

   