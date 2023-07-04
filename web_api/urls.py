
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.Registration.as_view()),
    path("addurl/", views.Addlink.as_view()),
    path("linkpage/", views.GetLinks.as_view(), name="linkpage"),
    path("countlink/<int:id>", views.countlink, name="countlink")
]
