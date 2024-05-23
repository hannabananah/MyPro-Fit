from django.contrib import admin
from .models import Deposit, Saving, Annuity
admin.site.register(Deposit)
admin.site.register(Saving)
admin.site.register(Annuity)
