from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

"""
Длина строк в БД по умолчанию
"""
DEFAULT_STRING_LENGTH = 120


class Address(models.Model):
    """
    Модель адреса
    Строковое представление Улица Дом
    Для номера дома установлены валидаторы,
    номер дома не может превышать 999 (таких длинных улиц будем считать, что не существует)
    и не может быть нулевым или отрицательным
    """
    street = models.CharField(max_length=DEFAULT_STRING_LENGTH)
    home = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(1)])

    def __str__(self):
        return f'{self.street} {self.home}'


class Shop(models.Model):
    """
    Модель магазина
    Я поставил в address у параметра on_delete значение CASCADE,
    поскольку решил, что раз удаляется адрес из базы данных,
    то и все соответствующие ему магазины тоже

    Я указал last_changed как NULLABLE, потому что
    решил, что при создании нового объекта магазина не может быть
    даты последнего изменения, то есть last_changed
    В задании не было прописано явно, какое именно поведение использовать:
    ставить NULL, или дату создания объекта, я решил ставить NULL
    """
    name = models.CharField(max_length=DEFAULT_STRING_LENGTH)
    address = models.ForeignKey('main.Address', on_delete=models.CASCADE, related_name="shops")
    last_changed = models.DateField(null=True)
