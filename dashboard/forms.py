from django import forms
from . models import *
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm


# NOTES FORM SECTION
class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

#HOMEWORK FORM SECTION
class DateInput(forms.DateInput):
    input_type = 'date'        
class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due': DateInput()}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']


# YOUTUBE SECTION FORM
        
class DashboardForm(forms.Form):
    text = forms.CharField(max_length = 100,label ='Enter Your Search  ')


# TODOO SECTION FORM
    

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_finished']




# BOOK SECTION FORM


class BooksDashboardForm(forms.Form):
    text = forms.CharField(max_length = 100,label ='Enter Your Search  ')



# DICTIONARY SECTION FORM
    

class DictionaryDashboardForm(forms.Form):
    text = forms.CharField(max_length = 100,label ='Enter Your Search  ')



# WIKIPEDIA SECTION FORM
    

class WikipediaDashboardForm(forms.Form):
    text = forms.CharField(max_length = 100,label ='Enter Your Search  ')


# CONVERSION SECTION FORM

class ConversionForm(forms.Form):
    CHOICES = [('length','Length'),('mass','Mass')]
    measurement = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect)
    
class ConversionLengthForm(forms.Form):
    CHOICES = [('yard','Yard'),('foot','Foot')]
    input = forms.CharField(required=False,widget=forms.TextInput(
        attrs={"type":"number","placeholder":"Enter The Number"}))
    measure1 = forms.CharField(
        label = '', widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(
        label = '', widget = forms.Select(choices = CHOICES)
    )

class ConversionMassForm(forms.Form):
    CHOICES = [('pound','Pound'),('kilogram','Kilogram')]
    input = forms.CharField(required=False,widget=forms.TextInput(
        attrs={"type":"number","placeholder":"Enter The Number"}))
    measure1 = forms.CharField(
        label = '', widget = forms.Select(choices = CHOICES)
    )
    measure2 = forms.CharField(
        label = '', widget = forms.Select(choices = CHOICES)
    )



# USER REGISTRATION FORM SECTION
    

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
