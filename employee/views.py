from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee
from django.db.models import Q

# # Create your views here.
# def Home(request):
#     return HttpResponse("Hello world")

# create view
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm()
    return render(request,'create.html',{'form':form})


# list view
def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'list.html',{'employees':employee})


# update view
def update_employee(request,pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request,'update.html',{'form':form})


# delete view
def delete_employee(request,pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('list')


# search view
def employee_list(request):
    query = request.GET.get('q', '').strip()
    employees = Employee.objects.all()

    if query:
        employees = employees.filter(
            Q(employee_id__icontains=query) |
            Q(employee_name__icontains=query) |
            Q(employee_email__icontains=query) |
            Q(employee_contact__icontains=query)
        )

    return render(request, 'list.html', {'employees': employees, 'query': query})