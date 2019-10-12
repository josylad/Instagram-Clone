from django import forms
from .models import Image, Comment


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
  
    
class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['Author', 'image_name', 'pub_date']
        

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['author', 'image', 'pub_date']
        widgets = {
          'comment': forms.Textarea(attrs={'rows':1, 'cols':10}),
        }
        