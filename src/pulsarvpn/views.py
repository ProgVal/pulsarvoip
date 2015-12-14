from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, RequestContext
from django.shortcuts import render
from django.views.generic import View
from pulsarvpn.models import SecretKeys

def welcome(request):

	return render(request,'welcomepage.html',locals())


def step1(request):

	return render(request,'step1.html',locals())


def step2(request):

	return render(request,'step2.html',locals())



def generate_keys(self, request, *args, **kwargs):
	path = "STATICFILES_DIRS.scripts.openvpn.sh"
	print path
	# send_mail('Subject here', 'Here is the message.', 'mail1@gmail.com', ['mail2@gmail.com'], fail_silently=False)
	return HttpResponse()