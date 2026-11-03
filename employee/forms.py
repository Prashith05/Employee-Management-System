from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = ('employee_id','employee_name',..)
        fields = '__all__'

    def clean_employee_email(self):
        email = self.cleaned_data['employee_email'].strip().lower()
        if Employee.objects.filter(employee_email=email).exists():
            raise forms.ValidationError("An employee with this email already exists.")
        return email

    def clean_employee_id(self):
        employee_id = self.cleaned_data.get('employee_id')
        if Employee.objects.filter(employee_id=employee_id).exists():
            raise forms.ValidationError("An employee with this ID already exists.")
        return employee_id

    def clean_employee_contact(self):
        employee_contact = self.cleaned_data.get('employee_contact')
        if Employee.objects.filter(employee_contact=employee_contact).exists():
            raise forms.ValidationError("An employee with this contact number already exists.")
        return employee_contact