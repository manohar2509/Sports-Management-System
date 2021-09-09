from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from basic_app import models
from django.http import HttpResponse
from django.core.mail import send_mail
class AthleteListView(ListView):
    context_object_name = 'athletes'
    model = models.UserProfileInfo
    template_name = 'basic_app/athlete_list.html'
class AthleteDetailView(DetailView):
    context_object_name = "athlete_detail"
    model = models.UserProfileInfo
    template_name = 'basic_app/athlete_detail.html'
class ResultMenListView(ListView):
    context_object_name = 'result_men'
    model = models.Result_Men
    template_name = 'basic_app/result_men.html'
class ResultWomenListView(ListView):
    context_object_name = 'result_women'
    model = models.Result_Women
    template_name = 'basic_app/result_women.html'
class MedalsListView(ListView):
    context_object_name = 'medals'
    model = models.Medals
    template_name = 'basic_app/medals.html'
def index(request):
    return render(request,'basic_app/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            send_mail('hello','hi1','chundurimanohar2509@gmail.com',[request.POST['email']])

            # Save User Form to Database
            user = user_form.save()
            print(request.POST['email'])
            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'basic_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_app/login.html', {})
