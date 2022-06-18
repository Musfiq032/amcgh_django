from homepage import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name= 'Home'
urlpatterns= [
        path('', views.home_view,name= 'Home'),
        # path('department_view/',department_view, name='department'),
        # path('service/',service_view,name='service'),
        # path('appointment/', appointment_view, name= 'appointment'),
        # path('contact/',contact_view, name= 'contact-us'),
        # path('blog/',blog_view, name='blog'),
        # path('about/',about_us_view,name= 'about'),
        # path('login_user/',views.user_login , name='login'),
        # path('register_user',views.register_view, name= 'register')

]