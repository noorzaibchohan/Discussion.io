from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Room, Topic


class RoomForm(ModelForm):
    topic = forms.CharField()

    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

    def clean_topic(self):
        topic_name = self.cleaned_data.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        return topic


class UserForm(ModelForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
    password = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Enter a Secure Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True, help_text='Re-enter the Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
