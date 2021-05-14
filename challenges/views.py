from django.http import response
from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "celebrate christmas",
    "february": "eat goose",
    'march': "hunt the deer",
    "april": "clean the house",
    "june": "clean the house",
    "july": "master Django!",
    "august": "stay cold",
    "september": "stay dry",
    "october": "eat pumpkin",
    "november": "avoid birds",
    "december": "kick a fat man"
}

def index(request):
    return render(request, "challenges/index.html", {
        "months": list(monthly_challenges.keys())
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
        return HttpResponseNotFound("<h2>This month is not supported</h2>")