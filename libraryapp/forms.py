from django import forms
from .models import Book
class BooksForm(forms.ModelForm):
	class Meta:
		model=Book
		fields=[
			"title",
			"author",
        ]
	
