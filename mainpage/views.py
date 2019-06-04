from django.shortcuts import render
from mainpage.models import Project, Technology
from . import forms
from django.core.mail import send_mail


from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

from django.core.mail import get_connection
from django.conf import settings

from .forms import ContactForm

def ProjectListAndFormView(request):
	projects = Project.objects.all()

	form = forms.ContactForm()
	if request.method == 'POST':
		form = forms.ContactForm(request.POST)
		if form.is_valid():
			sender_name = form.cleaned_data['name']
			sender_email = form.cleaned_data['email']

			message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
			send_mail('New Enquiry', message, sender_email, ['wihardjo.nathaniel@gmail.com'], fail_silently=False)

	context = {
		'projects': projects,
		'form': form, 
	}

	return render(request, 'main.html', context)
	
"""
class _ProjectListAndFormView(SuccessMessageMixin, ListView, FormView):
	model = Project # data from database
	template_name = 'main.html'
	context_object_name = 'list_projects' # name of the var in html template
    	queryset = Project.objects.all().order_by("-pub_date")#  list of all projects
    	object_list = None

    	form_class = ContactForm
    	success_url = '/' # After submiting the form keep staying on the same url
    	success_message = 'Your Form has been successfully submitted!'

    	def form_valid(self, form):
    	    # This method is called when valid form data has been POSTed.
    	    cd = form.cleaned_data
    	    con = get_connection('django.core.mail.backends.console.EmailBackend')
    	    send_mail(
    	        cd['name'],
    	        cd['message'],
    	        cd.get('email', 'noreply@example.com'),
    	        ['wihardjo.nathaniel@gmail.com'],
    	        fail_silently=False
    	    )
    	    return super(ProjectListAndFormView, self).form_valid(form)
"""
