from django import forms
from basic.blog.models import Post
from django.contrib.admin import widgets
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
 
class PostForm(forms.ModelForm):
    publish = forms.CharField(widget=widgets.AdminSplitDateTime())
    body = forms.CharField(widget=TinyMCE())
    
    def clean_publish(self):
        return filter(lambda c: not c in "u[],\'", self.cleaned_data['publish'])
    
    class Meta:
        model = Post
        
class FlatPageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())
    
    class Meta:
        model = FlatPage