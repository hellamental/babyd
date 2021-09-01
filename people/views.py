from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import People, Media, Images
from .forms import NameForm, MediaForm, ImageForm, UserRegisterForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
	context = {}
	return render(request, 'people/home.html', context)

def index(request):
    people_list = People.objects.all()
    user_list = User.objects.all()
    context = {'people_list':people_list,'user_list':user_list}
    return render(request, 'people/index.html', context)

def individual(request, person_id):
	person = People.objects.get(pk=person_id)
	media_list = Media.objects.all().filter(person=person)
	image_list = Images.objects.all().filter(person=person)
	print(media_list)
	context = {'person': person,'media_list': media_list, 'image_list':image_list}
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
	image_list = Images.objects.all().filter(person=person)
	print(media_list)

	#if this is a POST request we need to process the form data
	if request.method == 'POST':
		#create a form instance and populate it with the data from the request
		mediaform = MediaForm(request.POST, request.FILES)
		#check whether it's valid:
		if mediaform.is_valid():
			#process data in the form.cleaned_data as required
			#...
			#redirect to a new URL:
			mediaform.save()
			print('responseredirect')
			return HttpResponseRedirect(reverse('individual', args=(person.id,)))

	#if a GET (or any other method) we'll create a blank form.
	else:
		mediaform = MediaForm()

	if request.method == 'POST':
		imageform = ImageForm(request.POST, request.FILES)
		if imageform.is_valid():
			#process data in the form.cleaned_data as required
			#...
			#redirect to a new URL:
			imageform.save()
			print('responseredirect')
			return HttpResponseRedirect(reverse('individual', args=(person.id,)))

	#if a GET (or any other method) we'll create a blank form.
	else:
		imageform = ImageForm()

	context = {'person': person,'media_list': media_list, 'image_list':image_list, 'mediaform':mediaform, 'imageform':imageform}
	return render(request, 'people/individual.html', context)

def comments(request):
	context = {
	'comments': Comment.objects.all()
	}
	return render(request, 'people/individual.html', context)

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!')
			return redirect('index')
	else:
		form = UserRegisterForm()
	return render(request, 'people/register.html', {'form': form})

def base(request):
	context = {}
	return render(request, 'people/base.html', context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')
