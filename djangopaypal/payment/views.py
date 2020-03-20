from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_cancelled(request):
    return render(request, 'payment/cancelled.html')


def payment_process(request):
    # What you want the button to do.

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL, #Here you can change the email.
        "amount": 'Give in your amount',
        "item_name":'Give item name',
        "invoice":'The invoice you wanted to give',
        "currency_code": 'INR',
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('payment:done')),
        "cancel_return": request.build_absolute_uri(reverse('payment:cancelled')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment/payment.html", context)
