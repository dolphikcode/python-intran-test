from django.shortcuts import render
from holiday.models import Holiday
from holiday import forms
from holiday.forms import UserForm, UserProfileInfoForm

# Authentication imports
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    # create tuple what to show
    index_list = Holiday.objects.order_by('vacation_begining')
    index_dict = {'index_records':index_list}
    # return data to template
    return render(request, 'holiday/index.html', context=index_dict )

@login_required
def special(request):
    # create tuple what to show
    index_dict = {'title':"Special site for you"}
    # return data to template
    return render(request, 'holiday/special.html', context=index_dict )

def form(request):
    form = forms.VacationForm()

    if request.method == 'POST':
        form = forms.VacationForm(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS")

    return render(request, 'holiday/form.html', {'form':form})

def register(request):
    title = "Dodaj użytkownika"
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid and profile_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_photo' in request.FILES:
                profile.profile_photo = request.FILES['profile_photo']

            profile.save()

            registered=True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'holiday/register.html',
                  {
                      'user_form': user_form,
                      'profile_form': profile_form,
                      'title': title,
                      'registered': registered,
                  })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("USER NOT ACTIVE!")
        else:
            print("Someone tried to sneakin ;-)")
            print("Username: {}, Password: {}".format(username,password))
            return HttpResponse("Invalid login details!")
    else:
        return render(request, 'holiday/login.html', {'title': 'Zaloguj się!'})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
