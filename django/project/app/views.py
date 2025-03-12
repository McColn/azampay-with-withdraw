# from django.shortcuts import render
# from django.http import JsonResponse
# import requests
# from .utils import get_azampay_token

# def azampay_payment(request):
#     token = get_azampay_token()
#     if not token:
#         return JsonResponse({"error": "Failed to get access token"}, status=400)

#     url = "https://sandbox.azampay.co.tz/azampay/mno/checkout"
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "accountNumber": "255748121594",  # Replace with actual phone number
#         "additionalProperties": {
#             "property1": None,
#             "property2": None
#         },
#         "amount": "1000",  # Replace with actual amount
#         "currency": "TZS",  # TZS for Tanzanian Shilling
#         "externalId": "123456",  # Unique transaction ID
#         "provider": "Mpesa"
#     }

#     response = requests.post(url, json=payload, headers=headers)

#     if response.status_code == 200:
#         return JsonResponse(response.json())
#     return JsonResponse({"error": "Payment request failed"}, status=400)

# END OF ORIGIN BELOW USE MODEL

from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
from .utils import get_azampay_token, generate_checksum
from .forms import AzamPayForm
from .models import Payment

# D E P O S I T
def azampay_payment(request):
    if request.method == "POST":
        form = AzamPayForm(request.POST)
        if form.is_valid():
            # Save payment details in database as pending
            payment = form.save(commit=False)
            payment.status = "Pending"
            payment.save()

            token = get_azampay_token()
            if not token:
                payment.status = "Failed"
                payment.save()
                return JsonResponse({"error": "Failed to get access token"}, status=400)

            url = "https://sandbox.azampay.co.tz/azampay/mno/checkout"
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }

            payload = {
                "accountNumber": payment.account_number,
                "additionalProperties": {
                    "property1": None,
                    "property2": None
                },
                "amount": str(payment.amount),
                "currency": payment.currency,
                "externalId": payment.external_id,
                "provider": payment.provider
            }

            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                # Update payment status on success
                response_data = response.json()
                payment.status = "Success"
                payment.transaction_id = response_data.get("transactionId", "")
                payment.save()
                return JsonResponse(response_data)
            else:
                payment.status = "Failed"
                payment.save()
                return JsonResponse({"error": "Payment request failed"}, status=400)
    else:
        form = AzamPayForm()

    return render(request, "app/azampay_payment.html", {"form": form})



def payment_success(request):
    return render(request, "app/payment_success.html")

def payment_cancel(request):
    return render(request, "app/payment_cancel.html")


# W I T H D R A W
def process_withdrawal(user_mobile, amount, reference_id):
    token = get_azampay_token()
    if not token:
        return {"error": "Failed to get access token"}
    
    # Construct the input string
    input_string = f"{user_mobile}|{amount}|{reference_id}"  # Modify based on API docs
    checksum = generate_checksum(input_string)  # Generate checksum
    print('Encrypted Checksum:', checksum)

    url = "https://api-disbursement-sandbox.azampay.co.tz/api/v1/azampay/disburse"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "source": {
            "countryCode": "TZ",
            "fullName": "Betting Company",
            "bankName": "Tigo",
            "accountNumber": "123456789",
            "currency": "TZS"
        },
        "destination": {
            "countryCode": "TZ",
            "fullName": "User Name",
            "bankName": "Tigo",
            "accountNumber": 255654123456,
            "currency": "TZS"
        },
        "transferDetails": {
            "type": "withdrawal",
            "amount": amount,
            "dateInEpoch": 1710400000
        },
        "externalReferenceId": reference_id,
        "checksum": checksum,  # Use the generated checksum here
        "remarks": "Betting withdrawal"
    }

    response = requests.post(url, headers=headers, json=payload)

    return response.json()


# Example usage
# response = process_withdrawal("255654123456", 10000, "withdraw123")
# print(response)
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def withdraw(request):
    if request.method == "POST":
        # Use request.POST instead of JSON
        user_mobile = request.POST.get("user_mobile")
        amount = request.POST.get("amount")
        reference_id = request.POST.get("reference_id")

        if not all([user_mobile, amount, reference_id]):
            return JsonResponse({"error": "Missing required parameters"}, status=400)

        response = process_withdrawal(user_mobile, int(amount), reference_id)
        return JsonResponse(response, safe=False)

    # return JsonResponse({"error": "Invalid request method"}, status=405)
    return render(request, "app/withdraw.html")
