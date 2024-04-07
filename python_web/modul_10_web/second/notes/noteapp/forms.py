from django.forms import ModelForm, CharField, TextInput
from .models import Tag, Note


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class NoteForm(ModelForm):
    name = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    description = CharField(min_length=10, max_length=150, required=True, widget=TextInput())

    class Meta:
        model = Note
        fields = ['name', 'description']
        exclude = ['tags']

# У класі Meta ми можемо створити зв'язок між полями нашої моделі та різними полями,
# які ми хочемо мати у нашій формі, причому порядок перелічення полів має значення.
