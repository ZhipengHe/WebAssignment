import logging
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import hashers
from django.db.models import Q

from SmartCommunity_1622441019.forms import *
from SmartCommunity_1622441019.models import *

# Create your views here.


def index(request):
    return render(request, 'SmartCommunity_1622441019/index.html')


def help(request):
    return render(request, 'SmartCommunity_1622441019/help.html')


def about(request):
    return render(request, 'SmartCommunity_1622441019/about.html')


def logout(request):
    try:
        if request.session['remember']:
            del request.session['logged']
            del request.session['type']
        else:
            request.session.flush()
        return HttpResponseRedirect('/')
    except:
        request.session.flush()
        return HttpResponseRedirect('/')


def createadmin(request):
    form = CreateAdmin(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.password = hashers.make_password(instance.password)
        instance.save()
    return render(request, 'SmartCommunity_1622441019/admincreate.html', {'form': form})


def info(request):
    form = AddInfo(request.POST or None)
    if form.is_valid():
        serviceProvider = form.save()
        logging.debug(serviceProvider.providerName)
        return HttpResponseRedirect('/')
    return render(request, 'SmartCommunity_1622441019/info.html', {'form': form})


def issue(request):
    form = AddIssue(request.POST or None)
    if form.is_valid():
        newIssue = form.save()
        logging.debug(newIssue.issueName)
        return HttpResponseRedirect('/')
    return render(request, 'SmartCommunity_1622441019/addissue.html', {'form': form})


def admin(request):
    form = AdminModel(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        admin = Admin_1622441019.objects.get(emailAddress__iexact=instance.emailAddress)
        request.session['logged'] = 2
        request.session['admin'] = admin.emailAddress
        if form.cleaned_data["rememberMe"]:
            request.session['remember'] = True
        else:
            request.session['remember'] = False
        logging.debug((form.cleaned_data["rememberMe"]))
        return HttpResponseRedirect('/')
    else:
        try:
            if request.session['remember']:
                form.fields['emailsAddress'].initial = request.session['admin']
                form.fields['rememberMe'].initial = True
        except:
            pass
    return render(request, 'SmartCommunity_1622441019/admin.html', {'form': form})


def login(request):
    form = LoginModel(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        user = User_1622441019.objects.get(emailAddress__iexact=instance.emailAddress)
        request.session['logged'] = 1
        request.session['user'] = user.emailAddress
        request.session['type'] = user.userType
        if form.cleaned_data["rememberMe"]:
            request.session['remember'] = True
        else:
            request.session['remember'] = False
        logging.debug(form.cleaned_data["rememberMe"])
        return HttpResponseRedirect('/')
    else:
        try:
            if request.session['remember']:
                form.fields['emailAddress'].initial = request.session['user']
                form.fields['rememberMe'].initial = True
        except:
            pass
    return render(request, 'SmartCommunity_1622441019/login.html', {'form': form})


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        request.session['logged'] = 1
        request.session['user'] = user.emailAddress
        request.session['type'] = user.userType
        request.session['remember'] = False
        user.password = hashers.make_password(user.password)
        user.save()
        return HttpResponseRedirect('/')
    return render(request, 'SmartCommunity_1622441019/register.html', {'form': form})


def user(request):
    form = EditProfile(request.POST or None)
    if form.is_valid():
        user = User_1622441019.objects.get(emailAddress__iexact=request.session['user'])
        user.firstName = form.cleaned_data['firstName']
        user.lastName = form.cleaned_data['lastName']
        user.password = hashers.make_password(form.cleaned_data['password'])
        user.save()
        return HttpResponseRedirect('/')
    return render(request, 'SmartCommunity_1622441019/editprofile.html', {'form': form})


def result(request):
    provider_info = Provider_1622441019.objects.all()
    context = {
        'provider_info': provider_info,
    }
    return render(request, 'SmartCommunity_1622441019/result.html', context)


def provider(request, id):
    info = Provider_1622441019.objects.get(providerID=id)
    context = {
        'info': info,
    }
    return render(request, 'SmartCommunity_1622441019/providerprofile.html', context)


def searched(request):
    global filtered, lname, ltype
    bool = False
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            lname = form.cleaned_data['Name']
            ltype = form.cleaned_data['Type']
            bool = True
            filtered = Provider_1622441019.objects.filter(Q(providerName=lname) | Q(providerType=ltype))
        else:
            filtered = ""
    else:
        form = SearchForm()
        filtered = ""
    context = {
        'filtered': filtered,
        'form': form,
        'bool': bool,
    }
    return render(request, 'SmartCommunity_1622441019/result.html', context, {'form': form})


def volunteer(request):
    volunteer_info = User_1622441019.objects.filter(userType='Volunteer')
    context = {
        'volunteer_info': volunteer_info,
    }
    return render(request, 'SmartCommunity_1622441019/volunteer.html', context)


def member(request):
    member_info = User_1622441019.objects.filter(userType='Member')
    context = {
        'member_info': member_info,
    }
    return render(request, 'SmartCommunity_1622441019/member.html', context)


def allissue(request):
    issue_info = Issue_1622441019.objects.all()
    context = {
        'issue_info': issue_info,
    }
    return render(request, 'SmartCommunity_1622441019/allissue.html', context)


def allprovider(request):
    provider_info = Provider_1622441019.objects.all()
    context = {
        'provider_info': provider_info,
    }
    return render(request, 'SmartCommunity_1622441019/provider.html', context)


def eachissue(request, id):
    info = Issue_1622441019.objects.get(issueID=id)
    context = {
        'info': info,
    }
    return render(request, 'SmartCommunity_1622441019/issueprofile.html', context)


