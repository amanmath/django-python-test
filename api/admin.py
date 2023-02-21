from django.contrib import admin
from .models import Item, Location

# will this change?
admin.site.register(Item)
admin.site.register(Location)
