from django import forms    
from .models import Media

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['person','file_name','uploaded_file','uploaded_image']