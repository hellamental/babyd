from django import forms    
from .models import Media, Images
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['person','file_name','uploaded_file','file_information']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['person','uploaded_image','image_title','image_caption']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        