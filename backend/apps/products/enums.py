from django.db import models


class ProductTypes(models.TextChoices):
    FOOD = 'food', "Food"
    DRINK = 'drink', "Drink"
