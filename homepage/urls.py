from django.conf.urls.static import static

from django.conf import settings
from homepage.views import (home_view,
                            blog_view,
                            about_us_view,
                            service_list_view,
                            doctor_list_view,
                            contact_view,
                            doctor_details,
                            gb_list_view,
                            department_details,
                            management_team_view,
                            service_details_view,
                            gallery_view,backgroundhistory,career,whoweare,missionvission)
from django.urls import path
from . import views

app_name = 'homepage'
urlpatterns = [
                  path('', home_view, name='Home'),
                  # path('department_view/',department_view, name='department'),
                  # path('service/',service_view,name='service'),
                  # path('appointment/', appointment_view, name= 'appointment'),
                  path('contact/', contact_view, name='contact-us'),
                  path('blog/', blog_view, name='blog'),
                  path('about/', about_us_view, name='about'),
                  path('gallery/', gallery_view, name='gallery'),
                  # path('login_user/', views.user_login, name='login'),
                  path('register_user', views.register_view, name='register'),
                  path('service_details/<int:id>', service_details_view, name='service_detail'),
                  path('service-list/', service_list_view, name='service-list'),
                  # path('service-insert/', service_insert_view),
                  # path('news/', views.blog_list_view, name='news'),
                  # path('<int:id>/', views.dynamic_lookup_view, name='news-details'),
                  path('doctor-list/', doctor_list_view, name='doctor-list'),
                  path('department_details/<int:id>/', department_details, name='department_details'),
                  # path('department-list/', department_list_view, name='department-list'),
                  path('doctor_details/<int:id>', doctor_details, name="doctor_details"),
                  path('gb_list/', gb_list_view, name="governing-body"),
                  path('mt_list/', management_team_view, name="management-team"),
                  path('career/', career, name="career"),
                  path('mission&vission/', missionvission, name="mission&vission"),
                  path('whoWeAre/', whoweare, name="whoWeAre"),
                  path('backgroundHistory/', backgroundhistory, name="backgroundHistory"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
