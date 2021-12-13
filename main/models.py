from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

"""
Длина строк в БД по умолчанию. Этого значение считаю достаточным
"""
DEFAULT_STRING_LENGTH = 120


class Address(models.Model):
    street = models.CharField(max_length=DEFAULT_STRING_LENGTH)
    home = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(1)])

    def __str__(self):
        return f'{self.street} {self.home}'


class Shop(models.Model):
    name = models.CharField(max_length=DEFAULT_STRING_LENGTH, unique=True)
    address = models.ForeignKey('main.Address', on_delete=models.CASCADE, related_name="shops")
    last_changed = models.DateField()
