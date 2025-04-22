# res/views.py

from django.shortcuts import render

def res_home(request):
    return render(request, 'res.html')  
