from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

DEFAULT_STRING_LENGTH = 120


class Address(models.Model):
    """
    Address model
    Building's number (home column) can be only in [1; 999]
    """
    street = models.CharField(max_length=DEFAULT_STRING_LENGTH)
    home = models.IntegerField(validators=[MaxValueValidator(999), MinValueValidator(1)])

    def __str__(self):
        return f'{self.street} {self.home}'


class Shop(models.Model):
    """
    Shop model
    Address is foreign key (many shops in one address, MANY-to-ONE relationship)
    ON DELETE has value CASCADE, because I've chosen this behaviour as the most appropriate

    Last changed is made nullable because I think that once shop is instantiated,
    there's no last_changed date.
    
    There's no instruction in task how to resolve this case.
    However, I consider this solution as the most appropriate
    """
    name = models.CharField(max_length=DEFAULT_STRING_LENGTH)
    address = models.ForeignKey('main.Address', on_delete=models.CASCADE, related_name="shops")
    last_changed = models.DateField(null=True)
