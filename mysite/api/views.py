from django.http import HttpResponse
from django.shortcuts import render

from api.models import UserProfile


def users(request):
    context = {}
    context["User_Profile_table"] = UserProfile.objects.all()
    return render(request, 'index.html', context)