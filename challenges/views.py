from django.http.response import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "celebrate christmas",
    "feb": "eat goose",
    'march': "hunt the deer",
    "april": "clean the house",
    "june": "clean the house",
    "july": "master Django!"
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"""
            <ul>
                {list_items}
            </ul>
        """
    return HttpResponse(response_data)

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