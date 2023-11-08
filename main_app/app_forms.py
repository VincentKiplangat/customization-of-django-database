from django import forms

from main_app.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model= Employee
        fields = "__all__"
        widgets={
           "dob":forms.DateInput(attrs={"type":"date", "min":"1990-01-01", "max":"2005-12-31"}),
           "salary":forms.NumberInput(attrs={"max":75000, "min":10000})
        }
        labels = {
            "dob": "Date Of Birth",
            "email": "Email Address"
        }

