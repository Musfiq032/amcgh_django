from django.shortcuts import render
from django.shortcuts import render, HttpResponse
# from .models import Doctor, Department, service, news, Author, Category
# from .forms import DepartmentForm, ServiceForm
from CustomAdminPanel.models import Doctors, Departments, Service

from django.db.models import Q


def home_view(request):
    department_home_view = Departments.objects.all()[:2]
    service_home_view = Service.objects.all()[:8]
    doctor_list = Doctors.objects.all()
    context = {
        'service_list': service_home_view,
        'doctor_list': doctor_list,
        'department_list': department_home_view
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


def doctor_details(request, doctor_id):
    request.session['doctor_id'] = doctor_id
    doctor = Doctors.objects.get(admin=doctor_id)
    context = {
        'doctor_details': doctor,
        "id": doctor_id,
        "username": doctor.admin.username
    }
    return render(request, "Doctors/doctor-single.html", context)


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


# def department_insert_view(request):
#     form = DepartmentForm()
#     if request.method == 'POST':
#         form = DepartmentForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'Department/department-insert.html', context)


# def success(request):
#     return HttpResponse('successfully uploaded')


# def department_list_view(request):
#     if request.method == 'GET':
#         queryset = Department.objects.all()
#         context = {
#             "dep_list": queryset
#         }
#     return render(request, "Department/department.html", context)
#
#
# def dynamic_lookup_view_dept(request, id):
#     obj = Department.objects.get(id=id)
#     context = {
#         'object': obj
#     }
#     return render(request, "Department/department-single.html", context)


# def department_list_view2(request):
#     if request.method == 'GET':
#         queryset = Department.objects.all()
#         context = {
#             "dep_list": queryset
#         }
#     return render(request, "Department/department_with_sidebar.html", context)


# Create your views here.
# def is_valid_queryparam(param):
#     return param != '' and param is not None
#
#
# def blog_list_view(request):
#     queryset = news.objects.all()
#     cat_list = Category.objects.all()
#     category = request.GET.get('category')
#     title_or_author_query = request.GET.get('title_or_author')
#
#     if is_valid_queryparam(title_or_author_query):
#         queryset = queryset.filter(Q(title__icontains=title_or_author_query)
#                                    | Q(author__name__icontains=title_or_author_query)
#                                    ).distinct()
#
#     if is_valid_queryparam(category) and category != 'Choose...':
#         queryset = queryset.filter(categories__name=category)
#     else:
#         news.objects.all()
#     context = {
#         "blog_list": queryset,
#         "cat_list": cat_list
#         # 'post_count': post_count
#     }
#     return render(request, "News&events/blog.html", context)


# def dynamic_lookup_view(request, id):
#     obj = news.objects.get(id=id)
#     context = {
#         'object': obj
#     }
#     return render(request, "News&events/blog-single.html", context)
#
#
# def service_insert_view(request):
#     form = ServiceForm()
#     if request.method == 'POST':
#         form = ServiceForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#
#     context = {
#         'form': form
#     }
#     return render(request, 'Services/service-insert.html', context)


def service_list_view(request):
    if 'q' in request.GET:
        q = request.GET['q']
        service_list = Service.objects.filter(service_name__icontains=q)
    else:
        service_list = Service.objects.all()

    context = {
        'service_list': service_list
    }
    return render(request, "Services/service.html", context)


def gb_list_view(request):
    return render(request, "governing_body.html")


# def dynamic_lookup_service_view(request, id):
#     obj = service.objects.get(id=id)
#     ser_list = service.objects.all()
#     context = {
#         'object': obj,
#         'service': ser_list
#     }
#     return render(request, "Services/service-detail.html", context)

def contact_view(request):
    return render(request, 'contact.html')
