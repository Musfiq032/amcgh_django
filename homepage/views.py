from django.shortcuts import render
from django.shortcuts import render, HttpResponse
# from .models import Doctor, Department, service, news, Author, Category
# from .forms import DepartmentForm, ServiceForm
from CustomAdminPanel.models import Doctors, Departments, Service, GoverningBody, ManagementTeam

from django.db.models import Q


def home_view(request):
    department_menu = Departments.objects.all()
    department_home_view = Departments.objects.all()[:2]
    service_home_view = Service.objects.all()[:8]
    doctor_list = Doctors.objects.all()
    context = {
        'service_list': service_home_view,
        'doctor_list': doctor_list,
        'department_list': department_home_view,
        'department_menu': department_menu
    }
    return render(request, 'homepage/index.html', context)


def blog_view(request):
    return render(request, 'News&events/blog-sidebar.html')


def about_us_view(request):
    return render(request, 'about.html')


def register_view(request):
    return render(request, 'User/register.html')


# def doctor_form_view(request):
#     form= DoctorForm()
#     if request.method == "POST":
#         form= DoctorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('doctor-insert')
#         else:
#             form = DoctorForm()
#
#     context = {
#         'form': form
#         }
#     return render(request, "Doctors/doc_insert.html", context)


def doctor_details(request, id):
    request.session['doctor_id'] = id
    obj = Doctors.objects.get(admin=id)
    doctor_details = Doctors.objects.all()
    context = {
        'object': obj,
        'doctor_details': doctor_details
    }
    return render(request, "Doctors/doctor-single.html", context)


def department_details(request, id):
    request.session['department_id'] = id
    department = Departments.objects.get(id=id)
    doctor_list = Doctors.objects.all()
    department_list = Departments.objects.all()
    departments = request.GET.get('departments')
    if departments is None:
        pass
    else:
        doctor_list = Doctors.objects.filter(department_id__department_name__icontains=departments)

    context = {
        'doctor_list': doctor_list,
        'department': department,
        'department_list': department_list,
        "id": id,
    }
    return render(request, "Department/department-single.html", context)


def is_valid_queryparam(param):
    return param != '' and param is not None


def doctor_list_view(request, *args, **kwargs):
    qs = Doctors.objects.all()

    department_list = Departments.objects.values_list('department_name', flat=True)

    name_contains_query = request.GET.get('name_contains')
    print(name_contains_query)

    if is_valid_queryparam(name_contains_query):
        qs = qs.filter(department_id__department_name__contains=name_contains_query)
    else:
        qs = Doctors.objects.all()

    context = {
        'queryset': qs,
        'department_list': department_list,

    }

    return render(request, "Doctors/doctor_list.html", context)


def service_list_view(request):
    if 'q' in request.GET:
        q = request.GET['q']
        filtered_service_list = Service.objects.filter(service_name__icontains=q)
    else:
        filtered_service_list = Service.objects.all()

    context = {
        's_list': filtered_service_list
    }
    return render(request, "Services/service.html", context)


def gb_list_view(request):
    gb = GoverningBody.objects.all()

    context = {
        'gb': gb
    }
    return render(request, "governing_body.html", context)


def management_team_view(request):
    management_team = ManagementTeam.objects.all()

    context = {
        'management_team': management_team
    }
    return render(request, "management_team.html", context)


def service_details_view(request, id):
    service = Service.objects.get(id=id)
    service_details = Service.objects.all()
    context = {
        'service': service,
        'service_details': service_details
    }
    return render(request, "Services/service-detail.html", context)


def contact_view(request):
    return render(request, 'contact.html')


def gallery_view(request):
    return render(request, 'gallary.html')
