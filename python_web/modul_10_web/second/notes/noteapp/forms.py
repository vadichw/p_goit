from django.forms import ModelForm, CharField, TextInput
from .models import Tag


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']
# У класі Meta ми можемо створити зв'язок між полями нашої моделі та різними полями, які ми хочемо мати у нашій формі, причому порядок перелічення полів має значення.