import simplejson as simplejson
from django.core.exceptions import ValidationError
from django.shortcuts import render
# from quote_generator.profiles.models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm, LoginForm

# Create your views here.
from .models import UserProfile
from ..quotes.models import Quote


@transaction.atomic
def register_user(request):
    logout(request)
    registered = False
    template = 'auth_user/register_user.html'
    if request.method == "GET":
        context = {
            'user_form': RegisterForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, template, context)
    else:
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.theme_profile = 1
            group = Group.objects.get(name='Regular user')
            user.groups.add(group)

            pic = 'profile_image'
            if pic in request.FILES:
                profile.profile_image = request.FILES[pic]
            profile.save()
            registered = True
            login(request, user)
            return redirect('index')
        else:
            print(user_form.errors, profile_form.errors)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
    }

    return render(request, template, context)



def get_redirect_url(params):
    redirect_url = params.get('return_url')
    return redirect_url if redirect_url else 'index'



def login_user(request):
    template = 'auth_user/login_user.html'
    user = None
    if request.method == "GET":
        login_form = LoginForm()
        context = {
            'login_form': login_form,
        }
        return render(request, template, context)

    login_form = LoginForm(request.POST)
    return_url = get_redirect_url(request.POST)
    if login_form.is_valid():
        user = login_form.save()
        login(request, user)
        return redirect(return_url)

    context = {
            'login_form': LoginForm(),
    }
    return render(request, template, context)


def logout_user(request):
    logout(request)
    return redirect('index')




def profile_home_page(request):
    template = 'auth_user/profile_home_page.html'
    user = User.objects.get(pk=request.user.id)
    profile = UserProfile.objects.get(pk=request.user.id)
    quotes_added_by_user = Quote.objects.filter(added_by=request.user.id)
    color_theme = profile.theme_profile
    # if request.user.groups.filter(name='Regular user').exists():



    context = {
        'profile': profile,
        'quotes_added_by_user': quotes_added_by_user,
        'color_theme': color_theme,
    }
    return render(request, template, context)

    # if not profile:
    #     template = 'all_quotes.html'
    #     return render(request, template)
    # template = 'profile_home_page.html'
    # return render(request, template)


def edit_profile(request, pk):
    template = 'auth_user/edit_profile.html'
    profile = UserProfile.objects.get(pk=pk)
    if request.method == "GET":
        form = ProfileForm(instance=profile)
        context = {
            'form': form,
        }
        return render(request, template, context)
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
        profile = form.save()
        profile.save()
        return redirect(profile_home_page)
    context = {
        'form': form,
    }
    return render(request, template, context)


