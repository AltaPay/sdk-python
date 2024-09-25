#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

MobilePay test script.

"""

import sys
import random

# Update this with real path and uncomment before use, please
# sys.path.append('/absolute_path_to/python-client-library')

# sdk path check
sdkPathExists = False
for path in sys.path:
    if path.endswith("/sdk-python"):
        sdkPathExists = True

if not sdkPathExists:
    print("Path to sdk-python does not exist, update your environment variable, or put sys.path.append('/absolute_path_to/sdk-python') before including altapay sdk modules")
    sys.exit()

from altapay import API, Payment, CreditCardWalletInitiateAppPayment

api = API(mode='test',account='API username', password='API Password',  url='https://testgateway.altapaysecure.com/merchant/')

payment = Payment(api=api)

params = {
    'terminal': 'AltapPay MobilePay Terminal',  # Update terminal name
    'shop_orderid': 'Example_MobilePay' + str(random.randint(1, 1000)),
    'amount': 5.5,
    'currency': 'DKK',
    'type': 'payment',

    'customer_info': {
        'email': 'myuser@mymail.com',
        'username': 'myuser',
        'cardholder_name': 'myuser',
        'customer_phone': '20123456',
        'bank_name': 'My Bank',
        'bank_phone': '+45 12-34 5678',
        'billing_firstname': 'Testperson-dk',
        'billing_lastname': 'Approved',
        'billing_city': 'Varde',
        'billing_region': 'DK',
        'billing_postal': '6800',
        'billing_country': 'DK',
        'billing_address': 'Sæffleberggate 56,1 mf',
        'shipping_firstname': 'Testperson-dk',
        'shipping_lastname': 'Approved',
        'shipping_city': 'Varde',
        'shipping_region': 'DK',
        'shipping_postal': '6800',
        'shipping_country': 'DK',
        'shipping_address': 'Sæffleberggate 56,1 mf',
    },

    'orderLines': [
        {
            'description': 'description 01',
            'itemId': 'id 01',
            'quantity': 1,
            'unitPrice': 1.1
        },
        {
            'description': 'description 02',
            'itemId': 'id 02',
            'quantity': 2,
            'unitPrice': 2.2
        }
    ],
}

payment.create(**params)

if payment.success:
    print("Success!")

    data = {
        "customer_info": {
            "cardholder_name": "asdasd",
            "client_accept_language": "en",
            "client_user_agent": "Mozilla/5.0 (Linux; Android 13; SM-A536B)",
            "client_ip": "172.0.0.1",
            "client_accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "client_java_enabled": "false",
            "client_color_depth": "24",
            "client_screen_height": "845",
            "client_screen_width": "384",
            "client_time_zone": "-60",
            "client_javascript_enabled": "true"
        }
    }

    mobileAppPayment=CreditCardWalletInitiateAppPayment(api=api)
    response = mobileAppPayment.create(appUrl=payment.app_url, **data)

    print(response)
else:
    print("Error code: " + str(payment.error_code))
    print("Error message: " + payment.error_message)

# All the data
# print(payment.__data__)
