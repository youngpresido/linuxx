from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return HttpResponse("<h1>you are welcome to my homepage!</h1>")

def contactpage(request):
	return HttpResponse("<p>Call Me: +123456789</p>")
