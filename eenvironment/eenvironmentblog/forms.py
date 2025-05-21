from django import forms
from .models import Discussion, Comment, Signature

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['title', 'description','arie_discutie']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class SignatureForm(forms.ModelForm):
    class Meta:
        model = Signature
        fields = ['nume', 'prenume', 'adresa_email', 'judet', 'numar_telefon']