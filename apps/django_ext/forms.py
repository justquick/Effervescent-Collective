from django import forms
from basic.blog.models import Post
from django.contrib.admin import widgets
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from flatblocks.models import FlatBlock


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE())
    
    class Meta:
        model = Post
        
class FlatPageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())
    
    class Meta:
        model = FlatPage
        
class FlatBlockForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())
    
    class Meta:
        model = FlatBlock