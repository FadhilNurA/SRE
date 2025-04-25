# res/views.py

from django.shortcuts import render

def res_home(request):
    return render(request, 'res.html')  

def handler404(request, exception: Exception):
    """Custom 404 handler that uses the exception parameter."""
    error_details = {
        'error_code': 404,
        'exception_message': str(exception) if str(exception) else 'Resource not found',
        'request_path': request.path
    }
    return render(request, '404.html', context=error_details, status=404)