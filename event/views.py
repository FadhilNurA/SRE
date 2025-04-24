from django.shortcuts import render


def pentahelix(request):
    return render(request, 'pentahelix.html')


def workshop(request):
    return render(request, 'workshop.html')


def field_trip(request):
    return render(request, 'field_trip.html')
