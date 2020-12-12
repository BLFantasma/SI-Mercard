from django.db import models


# Create your models here.
class Products(models.Model):
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

    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    images = models.ImageField()
    tipo = models.CharField(max_length=30, choices= mytipo)
    country = models.CharField(max_length=120)
    quantity = models.PositiveSmallIntegerField()
    Language = models.CharField(max_length=120)
    Card_condition = models.CharField(max_length=30, choices= mycardconditions)
    Game_condition = models.CharField(max_length=30, choices= myGameconditions)