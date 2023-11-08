from django.shortcuts import render, redirect

from main_app.app_forms import EmployeeForm
from main_app.models import Employee


# Create your views here.
def home(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = EmployeeForm()
    return render(request, "employees.html", {"form": form})

#Model View Template
#
def employee_details(request, emp_id):
    employee = Employee.objects.get(pk=emp_id)  #select * FROM employees WHERE id=1
    return render(request, "employee_details.html", {"employee":employee })

def all_employees(request):
    employees = Employee.objects.all()  #SELECT * FROM employees
    return render(request, "all_employees.html", {"employees":employees})

