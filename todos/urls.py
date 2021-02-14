# Add this file to the main urls.py
from django.urls import path
from . import views


"""
>urlpatterns< a set name
path(): ("URL", views.its_function)

"""

#URLconf
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.month_number_todo),
    path("<str:month>", views.month_todo, name="url_month")
]