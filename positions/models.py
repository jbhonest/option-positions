from django.db import models


class Option(models.Model):
    OPTION_TYPE_CHOICES = [
        ('C', 'Call'),
        ('P', 'Put'),
    ]

    symbol = models.CharField(max_length=10)  # Ticker symbol
    option_type = models.CharField(
        max_length=1, choices=OPTION_TYPE_CHOICES)  # Call or Put
    expiration_date = models.DateField()  # Expiration date of the option
    strike = models.PositiveIntegerField()  # Strike price of the option
    bid = models.PositiveIntegerField()  # Bid price
    ask = models.PositiveIntegerField()  # Ask price

    def __str__(self):
        return f"{self.symbol} {self.get_option_type_display()} {self.strike} Exp {self.expiration_date}"
