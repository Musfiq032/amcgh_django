from django.conf.urls.static import static

from django.conf import settings
from homepage.views import (home_view, blog_view, about_us_view, service_insert_view,
                            service_list_view,
                            dynamic_lookup_view,
                            dynamic_lookup_view_dept,
                            doctor_list_view,
                            department_list_view,
                            department_list_view2, doctor_details)
from django.urls import path
from . import views

app_name = 'homepage'
urlpatterns = [
                  path('', home_view, name='Home'),
                  # path('department_view/',department_view, name='department'),
                  # path('service/',service_view,name='service'),
                  # path('appointment/', appointment_view, name= 'appointment'),
                  # path('contact/',contact_view, name= 'contact-us'),
                  path('blog/', blog_view, name='blog'),
                  path('about/', about_us_view, name='about'),
                  path('login_user/', views.user_login, name='login'),
                  path('register_user', views.register_view, name='register'),
                  path('<int:id>/', dynamic_lookup_view, name='service-detail'),
                  path('service-list/', service_list_view, name='service-list'),
                  path('service-insert/', service_insert_view),
                  path('news/', views.blog_list_view, name='news'),
                  path('<int:id>/', views.dynamic_lookup_view, name='news-details'),
                  # path('<int:id>/', dynamic_lookup_view_doc, name='doctor-detail'),
                  path('doctor-list/', doctor_list_view, name='doctor-list'),
                  path('department/<int:id>/', dynamic_lookup_view_dept, name='department-detail'),
                  path('department-list/', department_list_view, name='department-list'),
                  path('department-list-2/', department_list_view2, name='department-list-2'),
                  path('doctor_details/<str:doctor_id>', doctor_details, name="doctor_details")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
