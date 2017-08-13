from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from first_app.models import Topic, AccessRecord, Webpage
from first_app.forms import UserForm, UserProfileInfoForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)

def other(request):
    context_dict = {'text':'hello world','number':100}
    return render(request, 'first_app/other.html', context_dict)

def relative(request):
    return render(request, 'first_app/relative.html')

def indexx(request):
    return render(request, 'first_app/indexx.html')

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/registration.html', {
                                                            'user_form':user_form,
                                                            'profile_form':profile_form,
                                                            'registered':registered
                                                           })

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('first_app:indexx'))
            else:
                return HttpResponse("<h2>Account not active</h2>")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("<h2>Invalid login details supplied!</h2>")

    else:
        return render(request, 'first_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:indexx'))

@login_required
def special(request):
    return HttpResponse("<h2>Only if logged in you can see the page</h2>")