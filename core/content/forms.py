from django import forms
from .models import Event, Category, Session


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'organizer', 'description', 'status', 'image', 'category', 'published_date']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description', 'status', 'published_date']


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['event', 'title', 'start_time', 'end_time']