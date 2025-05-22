from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Categories(models.Model):
    name = models.CharField(verbose_name='Категории',max_length=20)

    def __str__(self):
        return f'{self.name}'


class Transaction(models.Model):
    TYPE_CHOICES = (
        ('Income', 'Доход'),
        ('Expense', 'Расход')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    date = models.DateField()
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.type} - {self.amount} ({self.category})'
    