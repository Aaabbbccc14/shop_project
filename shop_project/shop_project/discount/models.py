from django.db import models

class Discount(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()  # Процент скидки
    is_active = models.BooleanField(default=True)  # Активность скидки

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"
