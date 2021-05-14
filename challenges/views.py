from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

monthly_challenges = {
    "january": "celebrate christmas",
    "feb": "eat goose",
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month -1]
    redirect_path = reverse("month_challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthy_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported ")