from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("""<html>
    <head>
    <title>My todo list!</title>
    </head>
    <body>
    <h1>todos:</h1>
    <p>Mow the lawn</p>
    <p>Backup your PC</p>
    <p>Buy some milk</p>
    </body>
    </htmel>""")