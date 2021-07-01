RATE_TYPE_USD = 0
RATE_TYPE_EUR = 1

RATE_TYPE_CHOICES = (
    (RATE_TYPE_USD, 'Dollar'),
    (RATE_TYPE_EUR, 'Euro'),
)

REQUEST_METHOD_GET = 0
REQUEST_METHOD_POST = 1

REQUEST_METHOD_CHOICES = (
    (REQUEST_METHOD_GET, 'GET'),
    (REQUEST_METHOD_POST, 'POST'),
)

REQUEST_METHOD_CHOICES_MAPPER = {value[1]: value[0] for value in REQUEST_METHOD_CHOICES}
