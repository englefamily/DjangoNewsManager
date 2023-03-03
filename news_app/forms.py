from django.forms import ModelForm, Textarea
from .models import NewsPost
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(ModelForm):
    content = forms.CharField(max_length=20000, required=False, widget=Textarea(attrs={"rows": 5}))

    class Meta:
        model = NewsPost
        fields = '__all__'


class CreateUser(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "email", "password1", "password2"]:
            self.fields[fieldname].help_text = None


    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

