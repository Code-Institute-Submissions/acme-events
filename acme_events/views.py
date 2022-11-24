from django.shortcuts import render


def handler404(request, exception):
    """
    Error Handler 404 - Page Not Found
    Code from Code Institute Tutorial
    """
    return render(request, "errors/404.html", status=404)


def handler500(request, exception):
    """
    Error Handler 500 - Internal Server Error
    Docs: https://docs.djangoproject.com/en/4.1/ref/urls/#handler500
    """
    return render(request, "errors/500.html", status=500)
