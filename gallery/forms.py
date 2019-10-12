from django import forms
from .models import Image, Comment, Profile
from django.contrib.auth.models import User


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
  
    
class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['Author', 'image_name', 'pub_date', 'author_profile', 'location']
        widgets = {
          'description': forms.Textarea(attrs={'rows':4, 'cols':10,}),
        }
        

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['author', 'image', 'pub_date']
        widgets = {
          'comment': forms.Textarea(attrs={'rows':1, 'cols':10}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
          'bio': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }