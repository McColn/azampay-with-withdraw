from django.db import models

class Payment(models.Model):
    PAYMENT_PROVIDERS = [
        ("Mpesa", "Mpesa"),
        ("Airtel", "Airtel"),
        ("Tigo", "Tigo"),
    ]

    account_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="TZS")
    external_id = models.CharField(max_length=50, unique=True)
    provider = models.CharField(max_length=10, choices=PAYMENT_PROVIDERS)
    status = models.CharField(max_length=20, default="Pending")
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.provider} Payment - {self.amount} {self.currency} ({self.status})"
