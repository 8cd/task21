from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def found(request, id=0):
	return HttpResponse("Found!")


def not_found(request):
	return HttpResponseNotFound("Not Found!")