from django import forms
from ckeditor.fields import CKEditorWidget
from CustomAdminPanel.models import Departments


class DateInput(forms.DateInput):
    input_type = "date"


class AddDoctorForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password", max_length=50,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    designation = forms.CharField(label="Designation", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    research_publication = forms.CharField(label="Research & Publication", widget=CKEditorWidget())

    department_list = []
    try:
        departments = Departments.objects.all()
        for department in departments:
            small_department = (department.id, department.department_name)
            department_list.append(small_department)
    except:
        department_list = []

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    department = forms.ChoiceField(label="Department", choices=department_list,
                                   widget=forms.Select(attrs={"class": "form-control"}))
    sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
    degree = forms.CharField(label="Degree", widget=forms.TextInput(attrs={"class": "form-control "}))
    profile_pic = forms.FileField(label="Profile Pic", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}))


class EditDoctorForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50,
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    designation = forms.CharField(label="Designation", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    research_publication = forms.CharField(label="Research & Publication", widget=CKEditorWidget())

    department_list = []
    try:
        departments = Departments.objects.all()
        for department in departments:
            small_department = (department.id, department.department_name)
            department_list.append(small_department)
    except:
        department_list = []

    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    department = forms.ChoiceField(label="Department", choices=department_list,
                                   widget=forms.Select(attrs={"class": "form-control"}))
    sex = forms.ChoiceField(label="Sex", choices=gender_choice, widget=forms.Select(attrs={"class": "form-control"}))
    degree = forms.CharField(label="Degree", widget=forms.TextInput(attrs={"class": "form-control "}))
    profile_pic = forms.FileField(label="Profile Pic", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}))


class AddDepartmentForm(forms.Form):
    department_name = forms.CharField(label="Department Name", max_length=50,
                                      widget=forms.TextInput(attrs={"class": "form-control"}))
    department_short_description = forms.CharField(label="Short Description", max_length=200,
                                                   widget=forms.TextInput(attrs={"class": "form-control"}))
    department_description = forms.CharField(label="Description", widget=CKEditorWidget())
    department_image = forms.FileField(label="Department Image", max_length=50,
                                       widget=forms.FileInput(attrs={"class": "form-control"}))


class EditDepartmentForm(forms.Form):
    department_name = forms.CharField(label="Department Name", max_length=50,
                                      widget=forms.TextInput(attrs={"class": "form-control"}))
    department_short_description = forms.CharField(label="Short Description", max_length=200,
                                                   widget=forms.TextInput(attrs={"class": "form-control"}))
    department_description = forms.CharField(label="Description", widget=CKEditorWidget())
    department_image = forms.FileField(label="Department Image", max_length=50,
                                       widget=forms.FileInput(attrs={"class": "form-control"}))


class AddServiceForm(forms.Form):
    service_name = forms.CharField(label="Service Name", max_length=50,
                                   widget=forms.TextInput(attrs={"class": "form-control"}))
    service_description = forms.CharField(label="Description", widget=CKEditorWidget())
    service_image = forms.FileField(label="Service Image", max_length=50,
                                    widget=forms.FileInput(attrs={"class": "form-control"}))


class EditServiceForm(forms.Form):
    service_name = forms.CharField(label="Service Name", max_length=50,
                                   widget=forms.TextInput(attrs={"class": "form-control"}))
    service_description = forms.CharField(label="Description", widget=CKEditorWidget())
    service_image = forms.FileField(label="Service Image", max_length=50,
                                    widget=forms.FileInput(attrs={"class": "form-control"}))


class AddMtForm(forms.Form):
    member_name = forms.CharField(label="Member Name", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    institution = forms.CharField(label="Institution Name", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    designation = forms.CharField(label="Designation", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Picture", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}))


class EditMtForm(forms.Form):
    member_name = forms.CharField(label="Member Name", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    institution = forms.CharField(label="Institution Name", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    designation = forms.CharField(label="Designation", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile Picture", max_length=50,
                                  widget=forms.FileInput(attrs={"class": "form-control"}))


class AddGBForm(forms.Form):
    member_name = forms.CharField(label="Member Name", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    institution = forms.CharField(label="Institution Name", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    designation = forms.CharField(label="Designation", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))


class EditGBForm(forms.Form):
    member_name = forms.CharField(label="Member Name", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    institution = forms.CharField(label="Institution Name", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    designation = forms.CharField(label="Designation", max_length=50,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))