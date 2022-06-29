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
                  path('add_service/', HODview.add_service, name="add_service"),
                  path('add_service_save/', HODview.add_service_save, name="add_service_save"),
                  path('add_doctor', HODview.add_doctor, name="add_doctor"),
                  path('add_doctor_save', HODview.add_doctor_save, name="add_doctor_save"),
                  path('add_mt', HODview.add_mt, name="add_mt"),
                  path('add_mt_save', HODview.add_mt_save, name="add_mt_save"),
                  path('add_gb', HODview.add_gb, name="add_gb"),
                  path('add_gb_save', HODview.add_gb_save, name="add_gb_save"),

                  path('manage_doctor', HODview.manage_doctor, name="manage_doctor"),
                  path('manage_service', HODview.manage_service, name="manage_service"),
                  path('manage_department', HODview.manage_department, name="manage_department"),
                  path('manage_mt', HODview.manage_mt, name="manage_mt"),
                  path('manage_gb', HODview.manage_gb, name="manage_gb"),


                  path('edit_mt/<str:mt_id>', HODview.edit_mt, name="edit_mt"),
                  path('edit_mt_save', HODview.edit_mt_save, name="edit_mt_save"),
                  path('edit_gb/<str:gb_id>', HODview.edit_gb, name="edit_gb"),
                  path('edit_gb_save', HODview.edit_gb_save, name="edit_gb_save"),
                  path('edit_doctor/<str:doctor_id>', HODview.edit_doctor, name="edit_doctor"),
                  path('edit_doctor_save', HODview.edit_doctor_save, name="edit_doctor_save"),
                  path('edit_department/<str:department_id>', HODview.edit_department, name="edit_department"),
                  path('edit_department_save', HODview.edit_department_save, name="edit_department_save"),

                  # # #     Staff URL Path
                  # path('staff_home', Staffviews.staff_home, name="staff_home"),
                  # path('staff_take_attendence', Staffviews.staff_take_attendence, name="staff_take_attendence"),
                  # path('student_home', Studentviews.student_home, name="student_home")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
