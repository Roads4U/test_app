from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic import CreateView, ListView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.forms.models import model_to_dict
from django.urls import reverse_lazy
from django.db.models import CharField, Value
from django.db.models import CharField, Value, Sum
from . import models
import json, urllib.parse
import re
import requests
import datetime
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django.db.models import Q
from django.db.models import Max
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from json import dumps

from .models import data_population
from django.db.models import Sum

@login_required()
def data_population_p(request):
    yr_ftch = data_population.objects.order_by('year').values('year').distinct()
    years_list = {}
    index_k = 0
    for row in yr_ftch:
        print(row["year"])
        years_list[row["year"]] = (row["year"])

    return render(request, 'index.html',{"years_list": years_list})

@login_required()
def data_population_aj(request):
    year = (request.GET["year"])
    yr_ftch = data_population.objects.order_by('year').values('year').distinct()
    country_ftch = data_population.objects.filter(year=year).order_by('country').values('country').distinct()
    country = {}
    years_list = {}
    index_k = 0
    for row in yr_ftch:
        print(row["year"])
        years_list[row["year"]] = (row["year"])
    print(year)
    for row in country_ftch:
        country[row["country"]] = index_k
        index_k+=1

    data_grp_ftch = data_population.objects.filter(year=year).values("country","province").annotate(Sum('population'))
    data_grp = []
    try:
        for row in data_grp_ftch:
            print(row)
            data_temp = {}
            data_temp["x"] = list(country.keys())
            data_temp["y"] = [0] * len(country)
            data_temp["y"][country[row["country"]]] = list([row["population__sum"]])[0]
            data_temp["name"] = row["province"]
            data_temp["type"] = "bar"

            data_grp.append((data_temp))

        return HttpResponse(json.dumps(data_grp), {"years_list": years_list})

    except Exception as e:
        print(e)
        return HttpResponse("Error")


