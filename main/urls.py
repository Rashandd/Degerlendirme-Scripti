from django.urls import path
from . import views

urlpatterns = [
    path("<str:id>", views.feedback_form, name="form"),
]