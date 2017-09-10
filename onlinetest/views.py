from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist  # This may be used instead of Users.DoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .forms import LoginForm, SignupForm, IdeaForm, SearchForm
# for older versoins of Django use:
# from django.core.urlresolvers import reverse
import ast
from .models import Users, Idea, Feedback
from django.utils.timezone import datetime

import random
#from Crypto.cipher import AES

# from main.forms import SignupForm,LoginForm,SearchForm#,AddTopicForm,AddOpinionForm,

marks = 0
ques_no = 0
questions = []

def index(request):
    return render(request, 'onlinetest/index.html')


def clientlogin(request):
    return render(request, 'onlinetest/clientlogin.html')

def clientregister(request):
    return render(request, 'onlinetest/clientregister.html')

def clientadmin(request):
    if request.session.has_key('user_id'):
        uid = request.session['user_id']
        try:
            user = Users.objects.get(pk=uid)
            return render(request, 'onlinetest/clientadmin.html', {'user_id': user})
        except Users.DoesNotExist:
            return render(request, 'onlinetest/clientlogin.html')
        except quesFile.DoesNotExist:
            return render(request, 'onlinetest/clientadmin.html')
    else:
        return render(request, 'onlinetest/clientlogin.html')

def addidea(request):
    if request.session.has_key('user_id'):
        uid = request.session['user_id']
        try:
            user = Users.objects.get(pk=uid)
            return render(request, 'onlinetest/addidea.html', {'user_id': user})
        except Users.DoesNotExist:
            return render(request, 'onlinetest/clientlogin.html')
        
    else:
        return render(request, 'onlinetest/clientlogin.html')

def submitidea(request):
    if request.session.has_key('user_id'):
        uid = request.session['user_id']
        #return HttpResponse('1 ' + request.POST.get('title') + '2 ' + request.POST.get('description') + '3 ' + request.POST.get('link') + '4 ' + request.POST.get('prototype_link') + '5 ' + request.POST.get('tag'))
        if request.method == 'POST':
            idea = IdeaForm(request.POST)
        if idea.is_valid():
            user = Users.objects.get(id=uid)
            if idea.cleaned_data.get('public').lower() == 'no':
                sta = 0
            else:
                sta = 1
            p = Idea(
                title=idea.cleaned_data.get('title'),
                description=idea.cleaned_data.get('description'),
                link=idea.cleaned_data.get('link'),
                prototype_link=idea.cleaned_data.get('prototype_link'),
                user=user,
                tag=idea.cleaned_data.get('tag'),
                public=str(sta),
            )
            p.save()
        else:
            return HttpResponse("error")    
        return HttpResponseRedirect(reverse('onlinetest:clientadmin'))
    else:
        return render(request, 'onlinetest/clientlogin.html')

def feedback(request):
    tabledata = Feedback.objects.filter()
    return render(request, 'onlinetest/feedback.html', {'tabledata': tabledata})


def viewidea(request):
    if request.session.has_key('user_id'):
        uid = request.session['user_id']
        if request.method != 'POST' and request.POST.get('my') == None:
            user=Users.objects.get(id=uid)
            tabledata = Idea.objects.filter(public='1')
            #return HttpResponse(str(user) + tabledata[0].user)
            return render(request, 'onlinetest/viewidea.html', {'tabledata': tabledata, 'user': str(user)})
        elif request.method == 'POST' and request.POST.get('my') != None:
            user=Users.objects.get(id=uid)
            tabledata = Idea.objects.filter(user=user)
            return render(request, 'onlinetest/viewidea.html', {'tabledata': tabledata, 'user': str(user)})
            return HttpResponse(tabledata)
        else:
            
            tabledata = Idea.objects.filter()
            #return HttpResponse(data.user)
            return render(request, 'onlinetest/viewidea.html', {'tabledata': tabledata})
    else:
        return render(request, 'onlinetest/clientlogin.html')

def submitfeedback(request):
    if request.session.has_key('user_id'):
        uid = request.session['user_id']
        
        if request.method == 'POST' and request.POST.get('feedback') != None:
            user=Users.objects.get(id=uid)
            now = str(datetime.now().strftime("%Y%m%d%H%M"))
            #return HttpResponse(str(datetime.now().strftime("%Y%m%d%H%M")) + str(user))
            p = Feedback(
                title=request.POST.get('title'),
                feedback=request.POST.get('feedback'),
                user=user,
                feedback_id=now,
                
            )
            p.save()
            tabledata = Idea.objects.filter(public='1')
            #return HttpResponse(data.user)
            return HttpResponseRedirect(reverse('onlinetest:viewidea'))
            return render(request, 'onlinetest/viewidea.html', {'tabledata': tabledata})
    else:
        return render(request, 'onlinetest/clientlogin.html')

def clientloginval(request):
    if request.method == 'POST':
        log = LoginForm(request.POST)
        if log.is_valid():
            try:
                user = Users.objects.get(email=log.cleaned_data.get('email'), pwd=log.cleaned_data.get('pwd'))
                request.session['user_id'] = user.id
                useremail = user.email
                return HttpResponseRedirect(reverse('onlinetest:clientadmin'))
            except Users.DoesNotExist:
                return HttpResponse("Wrong Username Password")


def clientlogout(request):
    try:
        del request.session['user_id']
        return HttpResponseRedirect(reverse('onlinetest:index'))
    except:
        pass
    return HttpResponseRedirect(reverse('onlinetest:index'))


def register(request):
    if request.method == 'POST':
        signup = SignupForm(request.POST)
        if signup.is_valid():
            p = Users(
                first_name=signup.cleaned_data.get('firstname'),
                email=signup.cleaned_data.get('email'),
                pwd=signup.cleaned_data.get('pwd'),
            )
            p.save()
            request.session['user_id'] = p.id
    return HttpResponseRedirect(reverse('onlinetest:clientadmin'))




def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        now = str(datetime.now().strftime("%Y%m%d%H%M"))
        ques_paper = quesFile.objects.create(ques_paper_id=now, client=str(request.session['user_id']))
        ques_paper.save()
        myfile = request.FILES['myfile']
        ext = myfile.name[myfile.name.rfind('.'):]
        fs = FileSystemStorage()
        filename = fs.save(now + ext, myfile)
        onlinetest.file_reader.file_to_db(filename, str(request.session['user_id']), now)
# return HttpResponse("now" + filename + "request.session['user_id']" + str(request.session['user_id']))
        uploaded_file_url = fs.url(filename)
        return render(request, 'onlinetest/clientadmin.html', {
            'uploaded_file_url': uploaded_file_url,
        })
    return render(request, 'onlinetest/clientadmin.html')


def studentmarksdisplay(request):
    sinfo = studentProfile.objects.all()
    smarks = studentMark.objects.all()
    return render(request, 'onlinetest/studentmarks.html', {'smarks': smarks, 'sinfo':sinfo})

