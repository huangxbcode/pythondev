#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# Create your views here.

def hello_world2(request):
    todos = [{'title': '数学作业',
              'important': 'Minor'},
             {'title': '语文作业，作文一篇',
              'important': 'High'},
             {'title': '英语作业',
              'important': 'Medium'},
             ]
    todohead = [{'head': '我的作业',
              'level': '重要性'},
             ]
    t = loader.get_template('index.tmpl')
    c = Context({'todos': todos, 'todohead': todohead})
    return HttpResponse(t.render(c))

def hello_world(request):
    return HttpResponse("""
    <html>
        <head>
            <title>黄雨文的作业!</title>
        </head>
        <body>
            <h1>黄雨文今天的作息时间列表:</h1>
            <p>数学作业</p>
            <p>语文作业，作文一篇</p>
            <p>英语作业</p>
        </body>
    </htmel>""")
    
