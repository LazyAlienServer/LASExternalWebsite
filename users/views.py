from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView


def logout_view(request):
    logout(request)
    return redirect('/')


class ProfileView(TemplateView):
    template_name = 'users/profile.html'
