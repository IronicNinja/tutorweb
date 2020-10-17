stripe_publishable_key = 'pk_test_51HcKhAG4dN6WRPBc45enHhddOKyxFCrgQSKA5JviKzeVbKae74Ni4jymQEAb629xuZl8UTkEzrKHsKMEBZMTfGRL00wS2glxMF'
stripe_secret_key = 'sk_test_51HcKhAG4dN6WRPBcF5hA6NMj0tvIhR3vHTZPZ9O3J9uzRN4r3Ek3PRTfrp5GUMBoxu42QkVtIokEPIwQFCNb4Z5500sY7sbjiT'

stripe_keys = {
    "secret_key": stripe_secret_key,
    "publishable_key": stripe_publishable_key
}

import stripe
stripe.api_key = stripe_keys['secret_key']