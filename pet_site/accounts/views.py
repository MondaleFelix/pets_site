from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.http import HttpResponseRedirect


class SignUpView(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy("login")
	template_name = "accounts/signup.html"

class LoginView(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy("login")
	template_name = "accounts/signup.html"



def index(request):
	return HttpResponseRedirect(reverse("index"))