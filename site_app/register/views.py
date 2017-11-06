from django.shortcuts import render_to_response, redirect, RequestContext, HttpResponse, render, RequestContext
from django.views.generic.base import View
from django.core.urlresolvers import reverse

# model
from .models import Member

#language
from django.utils.translation import activate

#setting
from django.conf import settings



class HomeView(View):
    #@require_connect
    def get(self, request, *args, **kwargs):
        ct = {}
        ct["register_status"] = "homee"
        if request.session.get('login_user'):
            ct["login_user_session"] = request.session['login_user']
        return render_to_response('home.html', context_instance=RequestContext(request, ct))

class LoginView(View):
    #@require_connect
    def get(self, request, *args, **kwargs):
        ct = {}
        ct["register_status"] = "login"
        if request.session.get('login_user'):
            ct["login_user_session"] = request.session['login_user']
        return render_to_response('login.html', context_instance=RequestContext(request, ct))

    def post(self, request, *args, **kwargs):
        p1 = Member.objects.filter(username=request.POST["username"]).exists()
        p2 = Member.objects.filter(password=request.POST["password"]).exists()
        if p1 and p2:
            user = Member.objects.get(username=request.POST["username"])
            request.session['login_user'] = user.id
        return redirect('/')

class RegisterView(View):
    #@require_connect
    def get(self, request, *args, **kwargs):
        ct = {}
        ct["register_status"] = "incomplete"
        if request.session.get('login_user'):
            ct["login_user_session"] = request.session['login_user']
        return render_to_response('register.html', context_instance=RequestContext(request, ct))

    #@require_connect
    def post(self, request, *args, **kwargs):
        ct = {}
        name = request.POST["name"]
        username = request.POST["username"]
        password = request.POST["password"]

        if not Member.objects.filter(username=username).exists():
            member_save = Member(
                name=name,
                username=username,
                password=password
            )
            member_save.save()
            ct['status'] = "complease"
            #request.session['login_user'] = member_save.id
        else:
            ct['status'] = "username_isexists"
            ct['message'] = username
            return render_to_response('register.html',context_instance=RequestContext(request, ct))

        
        
        return redirect(reverse("frontend_home"))

def login(request, *args, **kwargs):
    if request.method == 'POST':
        p1 = Member.objects.filter(username=request.POST["username"]).exists()
        p2 = Member.objects.filter(password=request.POST["password"]).exists()

        if p1 and p2:
            user = Member.objects.get(username=request.POST["username"])
            request.session['login_user'] = user.id

    return redirect('/')    


def logout(request, *args, **kwargs):
    if 'login_user' in request.session:
        del request.session['login_user']
        
    return redirect('/')