"""
Registering models with the Django admin.
Registered models can be managed and viewed through the admin interface.

"""

from django.contrib import admin
from .models import Letting
from .models import Address

admin.site.register(Letting)
admin.site.register(Address)
