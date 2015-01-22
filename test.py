
def run():
	print("Run")
	

import os

from django.core.wsgi import get_wsgi_application
print ("Runig test...")
os.environ['DJANGO_SETTINGS_MODULE'] = 'amigosExtraviados.settings'
application = get_wsgi_application()
run()
