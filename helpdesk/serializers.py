from rest_framework import serializers
# from views import send_new_ticket_request
# from django.conf import settings
from . import models
import re


class TicketSystemSerializer(serializers.ModelSerializer):
    def validate_email(self, value):
        regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(regex_email, value):
            raise serializers.ValidationError("Invalid email format.")

        return value

    def validate_phone(self, value):
        regex_phone = r'^[6-9][0-9]{9}$'

        if not re.match(regex_phone, value):
            raise serializers.ValidationError("Invalid phone number format.")

        return value

    class Meta:
        model = models.TicketSystem
        fields = ['name', 'email', 'phone', 'message']




