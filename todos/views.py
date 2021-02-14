from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse


# Create your views here.
todos = {
    "january" : "Get the sun outside everyday for 10 minutes as soon as you wake up",
    "february" : "Add 20 minutes of cardio to workout",
    "march" : "Drink 2L of water everyday",
    "april" : "Take a long walk around the neighborhood",
    "may" : "Wake up everyday at 5:00am",
    "june" : "Read/finish a book",
    "july" : "Learn another programming skills. (It can be anything)",
    "august" : "Meditate everyday for 30 minutes",
    "september" : "Make a small programming project",
    "october" : None,
    "november" : "Go to TT Lounge and get a taro boba (in large size!)",
    "december" : "Write a journal everyday before bed",
}

def index(request):
    list_values = ""
    months = list(todos.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("url_month", args=[month])
        list_values += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = render(request, "todos/index.html", {
        "months" : months
    })
    
    return HttpResponse(response_data)

def month_number_todo(request, month):
    todos_key = list(todos.keys())
    the_month = todos_key[month-1]
    
    if month > len(todos):
        return HttpResponseNotFound("Check if you typed in right month!")
    
    redirect_path = reverse("url_month", args=[the_month])
    return HttpResponseRedirect(redirect_path)
    
    """
    HttpResponseRedirect: '/url/' + the designated url
    return HttpResponseRedirect('/todos/' + the_month)
    
    This can possibly be a problem because if we were to change the url (which is done in urls.py from goal2018),
    we should fix everything that is related to the url in hard code
    Use reverse from django.urls so that it re-direct to the directed view
    """



def month_todo(request, month):
    try:
        todo_month = todos[month]
        response_data = render(request, "todos/todo.html", {
            "text": todo_month,
            "month" : month.capitalize()
        })
        return HttpResponse(response_data)
    except:
        return Http404()