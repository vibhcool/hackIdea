import datetime
from django import forms


class SignupForm(forms.Form):
    firstname = forms.CharField(max_length=30)
    email = forms.CharField(max_length=120)
    pwd= forms.CharField(max_length=80)

class LoginForm(forms.Form):
    email=forms.CharField(max_length = 80)
    pwd= forms.CharField(max_length=80)

class IdeaForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=1000)
    link = forms.CharField(max_length=400)
    prototype_link = forms.CharField(max_length=400)
    public = forms.CharField(max_length=20)
    tag = forms.CharField(max_length=40)

"""
class AddTopicForm(forms.Form):
    topic_text=forms.CharField(max_length = 250)
    topic_desc=forms.CharField(max_length = 700)
    tag_text=forms.CharField(max_length = 250)

class AddOpinionForm(forms.Form):
    opinion_text=forms.CharField(max_length = 500)
    topic = forms.CharField(max_length = 5)
"""


class SearchForm(forms.Form):
    topic_text=forms.CharField(max_length = 250)
    #symptom=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,required=False)


class TestIdVal(forms.Form):
    test_id=forms.CharField(max_length = 250)
