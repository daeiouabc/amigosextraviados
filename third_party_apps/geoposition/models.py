from __future__ import unicode_literals
from django.conf import settings

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^geoposition\.fields\.GeopositionField"])
except ImportError:
    pass
