from django.shortcuts import render

def practice(request):
    return render(request, "ktms_app/practice.html")