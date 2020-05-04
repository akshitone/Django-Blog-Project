from django import forms

class ContactForm(forms.Form):
    txtname     = forms.CharField()
    txtemail    = forms.EmailField()
    txtcontent  = forms.CharField(widget=forms.Textarea)