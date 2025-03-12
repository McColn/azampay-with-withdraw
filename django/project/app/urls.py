from django.urls import path
from . import views
from .views import azampay_payment, payment_success, payment_cancel,process_withdrawal, withdraw

urlpatterns = [
    # path("azampay-payment/", azampay_payment, name="azampay_payment"),
    
    path("azampay/", azampay_payment, name="azampay_payment"),
    path("payment-success/", payment_success, name="payment_success"),
    path("payment-cancel/", payment_cancel, name="payment_cancel"),

    # withdraw
    path("process_withdrawal/", process_withdrawal, name="process_withdrawal"),

    path("withdraw/", views.withdraw, name="withdraw"),


]
