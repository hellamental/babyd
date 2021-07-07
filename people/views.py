from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import People, Media
from .forms import NameForm, MediaForm
from django.urls import reverse

# Create your views here.
def index(request):
    people_list = People.objects.all()
    context = {'people_list':people_list,}
    return render(request, 'people/index.html', context)

def individual(request, person_id):
	person = People.objects.get(pk=person_id)
	media_list = Media.objects.all().filter(person=person)
	print(media_list)
	context = {'person': person,'media_list': media_list}
	return render(request, 'people/individual.html', context)

def get_name(request):
	#if this is a POST request we need to process the form data
	if request.method == 'POST':
		#create a form instance and populate it with the data from the request
		form = MediaForm(request.POST, request.FILES)
		#check whether it's valid:
		if form.is_valid():
			#process data in the form.cleaned_data as required
			#...
			#redirect to a new URL:
			form.save()
			return HttpResponseRedirect('/')

	#if a GET (or any other method) we'll create a blank form.
	else:
		form = MediaForm()

	return render(request,'people/name.html', {'form':form})

def get_individual2(request, person_id):
	person = People.objects.get(pk=person_id)
	media_list = Media.objects.all().filter(person=person)
	print(media_list)

	#if this is a POST request we need to process the form data
	if request.method == 'POST':
		#create a form instance and populate it with the data from the request
		form = MediaForm(request.POST, request.FILES)
		#check whether it's valid:
		if form.is_valid():
			#process data in the form.cleaned_data as required
			#...
			#redirect to a new URL:
			form.save()
			print('responseredirect')
			return HttpResponseRedirect(reverse('individual', args=(person.id,)))

	#if a GET (or any other method) we'll create a blank form.
	else:
		form = MediaForm()

	context = {'person': person,'media_list': media_list, 'form':form}
	return render(request, 'people/individual.html', context)