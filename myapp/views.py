# views.py
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied



@login_required
def edit_user(request):
    user = User.objects.get(pk=request.user.pk)
    user_form = UserProfileForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('numDoc', 'firsrtName', 'lastName', 'phone', 'municipality', 'address'))
    formset = ProfileInlineFormset(instance=user)

    if request.method == "POST":
        user_form = UserProfileForm(request.POST, request.FILES, instance=user)
        formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

        if user_form.is_valid():
            created_user = user_form.save(commit=False)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

            if formset.is_valid():
                created_user.save()
                formset.save()
                return HttpResponseRedirect('/accounts/profile/')

    return render(request, "edit.html", {
        "noodle": request.user.pk,
        "noodle_form": user_form,
        "formset": formset,
    })




def home(request):
	msj = "Hello index."
	return render(request, 'index.html', {'msj': msj,})
	#return HttpResponse(template.render(context, request))

@login_required
def uprofile(request):

    user = User.objects.get(pk=request.user.pk)
    user_form = UserProfile.objects.get(user=user)

    titulo = user.pk
    msj = {
    "pk": user.pk,
    "name": user.username,
    'numDoc': user_form.numDoc, 
    'firsrtName': user_form.firsrtName, 
    'lastName':user_form.lastName, 
    'phone': user_form.phone, 
    'municipality':user_form.municipality, 
    'address': user_form.address,

    #"last": user.last,
    } 
    return render(request, 'profile.html', {'msj': msj,})
#return HttpResponse(template.render(context, request))

