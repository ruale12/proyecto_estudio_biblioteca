from django import forms;
from .models import Author, Book;

class AuthoForm(forms.ModelForm):
    class Meta:
        model: Author;
        fields = ["name","last_name","nationality","description"];

class BookForm(forms.ModelForm):
    class Meta:
        model: Book;
        fields = ["name","put_date","author_id"];
