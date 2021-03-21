from django.forms import ModelForm
from movies.models import Genre

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'