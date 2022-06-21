from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
from CustomAdminPanel.EmailBackEnd import EmailBackEnd


def showLoginPage(request):
    return render(request, "login_page.html")


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")

    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"),
                                         password=request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect("/admin_home")
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staff_home"))
            elif user.user_type == "3":
                return HttpResponseRedirect(reverse("student_home"))
            # return HttpResponse("Email : " +request.POST.get("email") + " Password : "+ request.POST.get("password"))

        else:
            messages.error(request, "Invalid Login Credentials")
            return HttpResponseRedirect("/login")


def GetUserDetails(request):
    if request.user != None:
        return HttpResponse("User :" + request.user.email + " usertype : " + request.user.user_type)
    else:
        return HttpResponse("Login First")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/login")
