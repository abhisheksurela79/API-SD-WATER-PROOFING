from django.contrib import admin
from . import models


# Register your models here.

class TicketSystemAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'email', 'phone', 'closed', 'created_at')
    search_fields = ('email', 'phone', 'ticket_id')  # Enable search by email, phone, or ticket_id


admin.site.register(models.TicketSystem, TicketSystemAdmin)
