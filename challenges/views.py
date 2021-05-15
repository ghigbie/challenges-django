from django.http import response
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string
from .data_set import *

def index(request):
    return render(request, "challenges/index.html", {
        "months": list(monthly_challenges.keys())
    })

def about(request):
    return render(request, "challenges/about.html", {
        "data": "this is an about page"
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h2>Invalid month</h2>")

    redirect_month = months[month -1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthy_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month.capitalize(),
            "text": challenge_text,
        })
    except:
       raise Http404("not found : (")