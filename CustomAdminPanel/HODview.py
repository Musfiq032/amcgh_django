from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from CustomAdminPanel.forms import AddDoctorForm, EditDoctorForm, AddDepartmentForm, EditDepartmentForm, AddServiceForm, \
    EditMtForm, EditServiceForm, AddMtForm, AddGBForm, EditGBForm, EditGalleryForm, AddGalleryForm, AddCategory, \
    EditCategory

from CustomAdminPanel.models import CustomUser, Doctors, Departments, Service, ManagementTeam, GoverningBody, \
    GalleryCategory, Gallery


def admin_home(request):
    return render(request, 'hod_template/home_content.html')


def add_department(request):
    form = AddDepartmentForm()
    return render(request, "hod_template/add_department_template.html", {"form": form})


def add_department_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = AddDepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            department_name = form.cleaned_data["department_name"]
            department_short_description = form.cleaned_data["department_short_description"]
            department_description = form.cleaned_data["department_description"]

            department_image = request.FILES['department_image']
            fs = FileSystemStorage()
            filename = fs.save(department_image.name, department_image)
            department_image_url = fs.url(filename)

            try:
                department_model = Departments(department_name=department_name,
                                               department_short_description=department_short_description,
                                               department_description=department_description)
                department_model.department_image = department_image_url
                department_model.save()
                messages.success(request, "Successfully Added Department")
                return HttpResponseRedirect(reverse("add_department"))
            except:
                messages.error(request, "Failed to Add Department")
                return HttpResponseRedirect(reverse("add_department"))
        else:
            form = AddDepartmentForm(request.POST)
            return render(request, "hod_template/add_department_template.html", {"form": form})


def add_service(request):
    form = AddServiceForm()
    return render(request, "hod_template/add_service_template.html", {"form": form})


def add_service_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = AddServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service_name = form.cleaned_data["service_name"]
            service_description = form.cleaned_data["service_description"]

            service_image = request.FILES['service_image']
            fs = FileSystemStorage()
            filename = fs.save(service_image.name, service_image)
            service_image_url = fs.url(filename)

            try:
                service_model = Service(service_name=service_name,
                                        service_description=service_description)
                service_model.service_image = service_image_url
                service_model.save()
                messages.success(request, "Successfully Added Service")
                return HttpResponseRedirect(reverse("add_service"))
            except:
                messages.error(request, "Failed to Add Service")
                return HttpResponseRedirect(reverse("add_service"))
        else:
            form = AddServiceForm(request.POST)
            return render(request, "hod_template/add_service_template.html", {"form": form})


def add_mt(request):
    form = AddMtForm()
    return render(request, "hod_template/add_mt_template.html", {"form": form})


def add_mt_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = AddMtForm(request.POST, request.FILES)
        if form.is_valid():
            member_name = form.cleaned_data["member_name"]
            designation = form.cleaned_data["designation"]
            institution = form.cleaned_data['institution']

            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)

            try:
                mt_model = ManagementTeam(member_name=member_name,
                                          designation=designation,
                                          institution=institution)
                mt_model.profile_pic = profile_pic_url
                mt_model.save()
                messages.success(request, "Successfully Added Member")
                return HttpResponseRedirect(reverse("add_mt"))
            except:
                messages.error(request, "Failed to Add Member")
                return HttpResponseRedirect(reverse("add_mt"))
        else:
            form = AddServiceForm(request.POST)
            return render(request, "hod_template/add_mt_template.html", {"form": form})


def add_gb(request):
    form = AddGBForm()
    return render(request, "hod_template/add_gb_template.html", {"form": form})


def add_gb_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = AddGBForm(request.POST, request.FILES)
        if form.is_valid():
            member_name = form.cleaned_data["member_name"]
            designation = form.cleaned_data["designation"]
            institution = form.cleaned_data['institution']

            try:
                gb_model = GoverningBody(member_name=member_name,
                                         designation=designation,
                                         institution=institution)
                gb_model.save()
                messages.success(request, "Successfully Added Member")
                return HttpResponseRedirect(reverse("add_gb"))
            except:
                messages.error(request, "Failed to Add Member")
                return HttpResponseRedirect(reverse("add_gb"))
        else:
            form = AddGBForm(request.POST)
            return render(request, "hod_template/add_gb_template.html", {"form": form})


def add_doctor(request):
    form = AddDoctorForm()
    return render(request, "hod_template/add_doctor_template.html", {"form": form})


def add_doctor_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = AddDoctorForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"]
            department_id = form.cleaned_data["department"]
            designation = form.cleaned_data["designation"]
            degree = form.cleaned_data["degree"]
            gender = form.cleaned_data["sex"]
            research_publication = form.cleaned_data['research_publication']

            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                      last_name=last_name, first_name=first_name, user_type=2)

                user.doctors.address = address
                department_obj = Departments.objects.get(id=department_id)
                user.doctors.department_id = department_obj
                user.doctors.designation = designation
                user.doctors.degree = degree
                user.doctors.gender = gender
                user.doctors.research_publication = research_publication
                user.doctors.profile_pic = profile_pic_url
                user.save()
                messages.success(request, "Successfully Added Doctor")
                return HttpResponseRedirect(reverse("add_doctor"))
            except:
                messages.error(request, "Failed to Add Doctor")
                return HttpResponseRedirect(reverse("add_doctor"))
        else:
            form = AddDoctorForm(request.POST)
            return render(request, "hod_template/add_doctor_template.html", {"form": form})


def dynamic_lookup_view_doc(request, id):
    obj = Doctors.objects.get(id=id)
    context = {
        'object': obj
    }
    return render(request, "Doctors/doctor-single.html", context)


def add_gallery(request):
    form = AddGalleryForm()
    return render(request, "hod_template/add_gallery_template.html", {"form": form})


def add_gallery_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = AddGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            image_name = form.cleaned_data["image_name"]
            category_id = form.cleaned_data['category']

            gallery_image = request.FILES['gallery_image']
            fs = FileSystemStorage()
            filename = fs.save(gallery_image.name, gallery_image)
            gallery_image_url = fs.url(filename)

            try:
                gallery_model = Gallery(image_name=image_name)

                category_obj = GalleryCategory.objects.get(id=category_id)
                gallery_model.category_id = category_obj
                gallery_model.gallery_image = gallery_image_url
                gallery_model.save()
                messages.success(request, "Successfully Added Image")
                return HttpResponseRedirect(reverse("add_gallery"))
            except:
                messages.error(request, "Failed to Add Image")
                return HttpResponseRedirect(reverse("add_gallery"))
        else:
            form = AddGalleryForm(request.POST)
            return render(request, "hod_template/add_gallery_template.html", {"form": form})


def add_category(request):
    form = AddCategory()
    return render(request, "hod_template/add_category_template.html", {"form": form})


def add_category_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = AddCategory(request.POST, request.FILES)
        if form.is_valid():
            category_name = form.cleaned_data["category_name"]

            try:
                category_model = GalleryCategory(category_name=category_name)

                category_model.save()
                messages.success(request, "Successfully Added Category")
                return HttpResponseRedirect(reverse("add_category"))
            except:
                messages.error(request, "Failed to Add Category")
                return HttpResponseRedirect(reverse("add_category"))
        else:
            form = AddCategory(request.POST)
            return render(request, "hod_template/add_category_template.html", {"form": form})


def manage_doctor(request):
    doctor = Doctors.objects.all()
    return render(request, 'hod_template/manage_doctor_template.html', {'doctor': doctor})


def manage_service(request):
    service = Service.objects.all()
    return render(request, 'hod_template/manage_service_template.html', {'service': service})


def manage_gallery(request):
    gallery = Gallery.objects.all()
    return render(request, 'hod_template/manage_gallery_template.html', {'gallery': gallery})


def manage_department(request):
    department = Departments.objects.all()
    return render(request, 'hod_template/manage_department_template.html', {'department': department})


def manage_mt(request):
    mt = ManagementTeam.objects.all()
    return render(request, 'hod_template/manage_mt_template.html', {'mt': mt})


def manage_gb(request):
    gb = GoverningBody.objects.all()
    return render(request, 'hod_template/manage_gb_template.html', {'gb': gb})


def edit_mt(request, mt_id):
    request.session['mt_id'] = mt_id
    mt = ManagementTeam.objects.get(id=mt_id)
    form = EditMtForm()
    form.fields['member_name'].initial = mt.member_name
    form.fields['institution'].initial = mt.institution
    form.fields['designation'].initial = mt.designation
    form.fields['profile_pic'].initial = mt.profile_pic

    return render(request, "hod_template/edit_mt_template.html",
                  {"form": form, "id": mt_id, "member_name": mt.member_name})


def edit_mt_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        mt_id = request.session.get('mt_id')
        form = EditMtForm(request.POST, request.FILES)
        if form.is_valid():
            member_name = form.cleaned_data["member_name"]
            institution = form.cleaned_data["institution"]
            designation = form.cleaned_data["designation"]

            if request.FILES.get('department_image', False):
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None
            try:
                mt = ManagementTeam.objects.get(id=mt_id)
                mt.member_name = member_name
                mt.institution = institution
                mt.designation = designation
                if profile_pic_url is not None:
                    mt.profile_pic = profile_pic_url
                mt.save()
                messages.success(request, "Successfully Edited Member Details")
                return HttpResponseRedirect(reverse("edit_mt", kwargs={"mt_id": mt_id}))
            except:
                messages.error(request, "Failed to Edit Member Details")
                return HttpResponseRedirect(reverse("edit_mt", kwargs={"mt_id": mt_id}))
        else:
            form = EditMtForm(request.POST)
            mt = ManagementTeam.objects.get(id=mt_id)
            return render(request, "hod_template/edit_mt_template.html",
                          {"form": form, "id": mt_id, "mt": mt})


def edit_gb(request, gb_id):
    request.session['gb_id'] = gb_id
    gb = ManagementTeam.objects.get(id=gb_id)
    form = EditGBForm()
    form.fields['member_name'].initial = gb.member_name
    form.fields['institution'].initial = gb.institution
    form.fields['designation'].initial = gb.designation

    return render(request, "hod_template/edit_gb_template.html",
                  {"form": form, "id": gb_id, "member_name": gb.member_name})


def edit_gb_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        gb_id = request.session.get('gb_id')
        form = EditGBForm(request.POST, request.FILES)
        if form.is_valid():
            member_name = form.cleaned_data["member_name"]
            institution = form.cleaned_data["institution"]
            designation = form.cleaned_data["designation"]

            try:
                gb = ManagementTeam.objects.get(id=gb_id)
                gb.member_name = member_name
                gb.institution = institution
                gb.designation = designation
                gb.save()
                messages.success(request, "Successfully Edited Member Details")
                return HttpResponseRedirect(reverse("edit_gb", kwargs={"gb_id": gb_id}))
            except:
                messages.error(request, "Failed to Edit Member Details")
                return HttpResponseRedirect(reverse("edit_gb", kwargs={"gb_id": gb_id}))
        else:
            form = EditMtForm(request.POST)
            gb = ManagementTeam.objects.get(id=gb_id)
            return render(request, "hod_template/edit_gb_template.html",
                          {"form": form, "id": gb_id, "gb": gb})


def edit_gallery(request, gallery_id):
    request.session['gallery_id'] = gallery_id
    gallery = ManagementTeam.objects.get(id=gallery_id)
    form = EditGalleryForm()
    form.fields['image_name'].initial = gallery.image_name
    form.fields['image'].initial = gallery.image
    form.fields['category'].initial = gallery.category

    return render(request, "hod_template/edit_gallery_template.html",
                  {"form": form, "id": gallery_id, "image_name": gallery.image_name})


def edit_gallery_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        gallery_id = request.session.get('gallery_id')
        form = EditGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            image_name = form.cleaned_data["image_name"]
            category = form.cleaned_data["category"]

            if request.FILES.get('profile_pic', False):
                image = request.FILES['image']
                fs = FileSystemStorage()
                filename = fs.save(image.image_name, image)
                image_url = fs.url(filename)
            else:
                image_url = None

            try:
                gallery = Gallery.objects.get(id=gallery_id)
                gallery.image_name = image_name
                category = GalleryCategory.objects.get(id=category)
                gallery.department_id = category
                gallery.image = image_url
                gallery.save()
                messages.success(request, "Successfully Edited Gallery")
                return HttpResponseRedirect(reverse("edit_gallery", kwargs={"gallery_id": gallery_id}))
            except:
                messages.error(request, "Failed to Edit Gallery")
                return HttpResponseRedirect(reverse("edit_gallery", kwargs={"gallery_id": gallery_id}))
        else:
            form = EditGalleryForm(request.POST)
            gallery = Gallery.objects.get(id=gallery_id)
            return render(request, "hod_template/edit_gallery_template.html",
                          {"form": form, "id": gallery_id, "gallery": gallery})


def edit_doctor(request, doctor_id):
    request.session['doctor_id'] = doctor_id
    doctor = Doctors.objects.get(admin=doctor_id)
    form = EditDoctorForm()
    form.fields['email'].initial = doctor.admin.email
    form.fields['first_name'].initial = doctor.admin.first_name
    form.fields['last_name'].initial = doctor.admin.last_name
    form.fields['username'].initial = doctor.admin.username
    form.fields['address'].initial = doctor.address
    form.fields['designation'].initial = doctor.designation
    form.fields['degree'].initial = doctor.degree
    form.fields['department'].initial = doctor.department_id.id
    form.fields['sex'].initial = doctor.gender
    form.fields['research_publication'].initial = doctor.research_publication

    return render(request, "hod_template/edit_doctor_template.html",
                  {"form": form, "id": doctor_id, "username": doctor.admin.username})


def edit_doctor_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        doctor_id = request.session.get("doctor_id")
        if doctor_id is None:
            return HttpResponseRedirect(reverse("manage_doctor"))

        form = EditDoctorForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            department_id = form.cleaned_data["department"]
            designation = form.cleaned_data["designation"]
            degree = form.cleaned_data["degree"]
            gender = form.cleaned_data["sex"]
            research_publication = form.cleaned_data['research_publication']

            if request.FILES.get('profile_pic', False):
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

            try:
                user = CustomUser.objects.get(id=doctor_id)
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email = email
                user.save()

                doctor = Doctors.objects.get(admin=doctor_id)
                doctor.address = address
                department = Departments.objects.get(id=department_id)
                doctor.department_id = department
                doctor.gender = gender
                doctor.degree = degree
                doctor.designation = designation
                doctor.research_publication = research_publication
                if profile_pic_url is not None:
                    doctor.profile_pic = profile_pic_url
                doctor.save()
                del request.session['doctor_id']
                messages.success(request, "Successfully Edited Doctor Details")
                return HttpResponseRedirect(reverse("edit_doctor", kwargs={"doctor_id": doctor_id}))
            except:
                messages.error(request, "Failed to Edit Student")
                return HttpResponseRedirect(reverse("edit_doctor", kwargs={"doctor_id": doctor_id}))
        else:
            form = EditDoctorForm(request.POST)
            doctor = Doctors.objects.get(admin=doctor_id)
            return render(request, "hod_template/edit_doctor_template.html",
                          {"form": form, "id": doctor_id, "username": doctor.admin.username})


#
def edit_department(request, department_id):
    request.session['department_id'] = department_id
    department = Departments.objects.get(id=department_id)
    form = EditDepartmentForm()
    form.fields['department_name'].initial = department.department_name
    form.fields['department_short_description'].initial = department.department_short_description
    form.fields['department_description'].initial = department.department_description

    return render(request, "hod_template/edit_department_template.html",
                  {"form": form, "id": department_id, "departmentname": department.department_name})


#
#
def edit_department_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        department_id = request.session.get('department_id')
        form = EditDepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            department_name = form.cleaned_data["department_name"]
            department_short_description = form.cleaned_data["department_short_description"]
            department_description = form.cleaned_data["department_description"]

            if request.FILES.get('department_image', False):
                department_image = request.FILES['department_image']
                fs = FileSystemStorage()
                filename = fs.save(department_image.name, department_image)
                department_image_url = fs.url(filename)
            else:
                department_image_url = None
            try:
                department = Departments.objects.get(id=department_id)
                department.department_name = department_name
                department.department_short_description = department_short_description
                department.department_description = department_description
                if department_image_url is not None:
                    department.department_image = department_image_url
                department.save()
                messages.success(request, "Successfully Edited Doctor Details")
                return HttpResponseRedirect(reverse("edit_department", kwargs={"department_id": department_id}))
            except:
                messages.error(request, "Failed to Edit Student")
                return HttpResponseRedirect(reverse("edit_department", kwargs={"department_id": department_id}))
        else:
            form = EditDepartmentForm(request.POST)
            department = Departments.objects.get(id=department_id)
            return render(request, "hod_template/edit_department_template.html",
                          {"form": form, "id": department_id, "department": department})

#
# def edit_course(request, course_id):
#     course = Course.objects.get(id=course_id)
#     return render(request, "hod_template/edit_course_template.html", {"course": course, "id": course_id})
#
#
# def edit_course_save(request):
#     if request.method != "POST":
#         return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         course_id = request.POST.get("course_id")
#         course_name = request.POST.get("course")
#
#         try:
#             course = Course.objects.get(id=course_id)
#             course.course_name = course_name
#             course.save()
#             messages.success(request, "Successfully Edited Course")
#             return HttpResponseRedirect(reverse("edit_course", kwargs={"course_id": course_id}))
#         except:
#             messages.error(request, "Failed to Edit Course")
#             return HttpResponseRedirect(reverse("edit_course", kwargs={"course_id": course_id}))

#
# def add_session_year(request):
#     session = SessionYearModel.objects.all()
#
#     return render(request, 'hod_template/session_year_template.html', {"session": session})
#
#
# def add_session_year_save(request):
#     if request.method != "POST":
#         return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         session_start_year = request.POST.get("session_start")
#         session_end_year = request.POST.get("session_end")
#
#         try:
#             sessionyear = SessionYearModel(session_start_year=session_start_year, session_end_year=session_end_year)
#             sessionyear.save()
#             messages.success(request, "Successfully Added Session Year")
#             return HttpResponseRedirect(reverse("add_session_year"))
#         except:
#             messages.error(request, "Failed to Add Session Year")
#             return HttpResponseRedirect(reverse("add_session_year"))
