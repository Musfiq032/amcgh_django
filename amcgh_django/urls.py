"""amcgh_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from CustomAdminPanel import views, HODview

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('homepage.urls')),
                  path('login/', views.showLoginPage, name="login"),
                  path('doLogin/', views.doLogin, name="doLogin"),
                  # path('get_user_details/', views.GetUserDetails, name="GetUserDetails"),
                  path('logout_user/', views.logout_user, name="logout"),
                  path('admin_home/', HODview.admin_home, name="admin_home"),
                  # path('add_staff/', HODview.add_staff, name="add_staff"),
                  # path('add_staff_save/', HODview.add_staff_save, name="add_staff_save"),
                  path('add_department/', HODview.add_department, name="add_department"),
                  path('add_department_save/', HODview.add_department_save, name="add_department_save"),
                  path('add_doctor', HODview.add_doctor, name="add_doctor"),
                  path('add_doctor_save', HODview.add_doctor_save, name="add_doctor_save"),
                  # path('add_subject', HODview.add_subject, name="add_subject"),
                  # path('add_subject_save', HODview.add_subject_save, name="add_subject_save"),
                  # path('manage_staff', HODview.manage_staff, name="manage_staff"),
                  path('manage_doctor', HODview.manage_doctor, name="manage_doctor"),
                  # path('manage_course', HODview.manage_course, name="manage_course"),
                  path('manage_department', HODview.manage_department, name="manage_department"),
                  # path('edit_staff/<str:staff_id>', HODview.edit_staff, name="edit_staff"),
                  # path('edit_staff_save', HODview.edit_staff_save, name="edit_staff_save"),
                  path('edit_doctor/<str:doctor_id>', HODview.edit_doctor, name="edit_doctor"),
                  path('edit_doctor_save', HODview.edit_doctor_save, name="edit_doctor_save"),
                  path('edit_department/<str:department_id>', HODview.edit_department, name="edit_department"),
                  path('edit_department_save', HODview.edit_department_save, name="edit_department_save"),
                  # path('edit_course/<str:course_id>', HODview.edit_course, name="edit_course"),
                  # path('edit_course_save', HODview.edit_course_save, name="edit_course_save"),
                  # path('add_session_year', HODview.add_session_year, name="add_session_year"),
                  # path('add_session_year_save', HODview.add_session_year_save, name="add_session_year_save"),
                  # # #     Staff URL Path
                  # path('staff_home', Staffviews.staff_home, name="staff_home"),
                  # path('staff_take_attendence', Staffviews.staff_take_attendence, name="staff_take_attendence"),
                  # path('student_home', Studentviews.student_home, name="student_home")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
