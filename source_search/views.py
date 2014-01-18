from django.http import HttpResponse
from django.template import loader, RequestContext

from django.shortcuts import redirect, render_to_response

def index(request):
    return render_to_response("index.html",
        {'message':'hi'},RequestContext(request))
