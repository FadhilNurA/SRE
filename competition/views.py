from django.shortcuts import render

def compe_bcc(request):
    return render(request, 'bcc.html')  

def compe_pcc(request):
    return render(request, 'pcc.html')

def compe_reic(request):
    return render(request, 'reic.html')