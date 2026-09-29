from django.db import models

status = models.CharField(max_length=20, default='Pending')

class Bookings(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    client = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
    )

    class Meta:
        managed = False
        db_table = 'bookings'
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return f"{self.client} — {self.service} ({self.date})"