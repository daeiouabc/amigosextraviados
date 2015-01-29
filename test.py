
def run():
    print("Run")
    factory = APIRequestFactory()
    request = factory.post('/api/user/1')
    print(request)


import os

from django.core.wsgi import get_wsgi_application
print ("Runig test...")
os.environ['DJANGO_SETTINGS_MODULE'] = 'amigosExtraviados.settings'
application = get_wsgi_application()

from rest_framework.test import APIRequestFactory
run()
