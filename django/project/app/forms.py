from django import forms
from .models import Payment

class AzamPayForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["account_number", "amount", "currency", "external_id", "provider"]
