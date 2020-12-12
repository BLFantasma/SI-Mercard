from django import forms

from .models import Products

class ProductsForm(forms.Form):
    mytipo = (
        ('GM', 'Console Game'),
        ('YGOC', 'Yugioh Card'),
        ('MGC', 'Magic Card'),
        ('PKMNC', 'Pokémon Card'),
    )

    mycardconditions = (
        ('NM','NM'),
        ('LP','LP'),
        ('MP','MP'),
        ('HP','HP'),
        ('D','D'),
    )

    myGameconditions = (
        ('Nw','New'),
        ('LN','Like-New'),
        ('US','Used'),
    )

    title = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'placeholder':'Digite o nome de seu produto'}))
    price =forms.DecimalField(min_value=0, max_digits=100, decimal_places=2, initial=0.00)
    images = forms.ImageField()
    tipo = forms.ChoiceField(choices= mytipo)
    country = forms.CharField(max_length=120)
    quantity = forms.IntegerField()
    Language = forms.CharField(max_length=120)
    Card_condition = forms.ChoiceField(choices= mycardconditions)
    Game_condition = forms.ChoiceField(choices= myGameconditions)