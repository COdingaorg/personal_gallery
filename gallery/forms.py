from django import forms

class NewsletterForm(forms.Form):
  user_name = forms.CharField(label='First Name :', max_length=30)
  email = forms.EmailField(label='Email')