from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from .forms import ProfileForm
from .models import UserProfile
from ..quotes.models import Quote
from ..quotes.views import base, get_the_image

UserModel = get_user_model()


@login_required
def profile_home_page(request):
    template = 'auth_user/profile_home_page.html'
    user = UserModel.objects.get(pk=request.user.id)
    profile = UserProfile.objects.get(pk=request.user.id)
    quotes_added_by_user = Quote.objects.filter(added_by=request.user.id)
    # color_theme = profile.theme_profile
    # if request.user.groups.filter(name='Regular user').exists():

    context = {
        'profile': profile,
        'quotes_added_by_user': quotes_added_by_user,
        # 'color_theme': color_theme,
    }
    return render(request, template, context)

    # if not profile:
    #     template = 'all_quotes.html'
    #     return render(request, template)
    # template = 'profile_home_page.html'
    # return render(request, template)


@login_required
def edit_profile(request, pk):
    template = 'auth_user/edit_profile.html'
    profile = UserProfile.objects.get(pk=pk)
    quotes_added_by_user = Quote.objects.filter(added_by=request.user.id)
    user = request.user
    if request.method == "GET":
        form = ProfileForm(instance=profile)
        context = {
            'form': form,
            'profile': profile,
            'quotes_added_by_user': quotes_added_by_user,
            'user': user
        }
        return render(request, template, context)

    current_pic = profile.image
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    new_pic = request.FILES.get('profile_image')
    if form.is_valid():
        profile.image = get_the_image(profile, current_pic, new_pic)
        profile = form.save(commit=False)
        profile.save()
        return redirect(profile_home_page)
    context = {
        'form': form,
        'profile': profile,
        'quotes_added_by_user': quotes_added_by_user,
    }
    return render(request, template, context)


@login_required
def delete_user(request, pk):
    template = 'auth_user/delete_profile.html'
    profile = UserProfile.objects.get(pk=pk)
    user = UserModel.objects.get(pk=pk)
    if request.method == "GET":
        form = ProfileForm(instance=profile)
        for name, field in form.fields.items():
            field.widget.attrs['disabled'] = True
        form.save(commit=False)
        context = {
            'form': form,

        }
        return render(request, template, context)
    if profile.image:
        image = profile.image
        image.delete()
    user.delete()
    profile.delete()
    return redirect(base)
