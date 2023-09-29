from django.conf import settings
from django.core.mail import send_mail
from rest_framework import generics
from . import models
from . import serializers


# Create your views here.

def send_new_ticket_request(to_email, from_email, subject, message):
    # Send the email
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=[to_email], fail_silently=True)



class NewTicket(generics.CreateAPIView):
    queryset = models.TicketSystem.objects.all()
    serializer_class = serializers.TicketSystemSerializer


    def perform_create(self, serializer):
        ticket = serializer.save()
        customer_subject = f'Your ticket - {ticket.ticket_id} has been successfully raised'
        customer_message = f'''Hi {ticket.name},

Thank you for raising a ticket with S.D Water Proofing. Your ticket has been successfully created and we will contact you soon to discuss your issue. 

In the meantime, please keep your ticket number handy so that we can reference it when we speak to you. Your ticket number is {ticket.ticket_id}. 

Thank you for your patience and understanding.

Sincerely,

The S.D Water Proofing Team'''

        send_new_ticket_request(to_email=ticket.email, from_email=settings.EMAIL_HOST_USER, subject=customer_subject,
                                message=customer_message)



        admin_subject = f'New ticket - {ticket.ticket_id} raised'
        admin_message = f'''Hi there,

A new ticket has been raised. The details of the ticket are as follows:

Ticket number: {ticket.ticket_id}
Customer name: {ticket.name}
Customer email: {ticket.email}
Customer phone number: {ticket.phone}
Ticket description: {ticket.message}
Please take a look at the ticket and assign it to an agent as soon as possible.

Thank you,

The S.D Water Proofing Team'''

        send_new_ticket_request(to_email=settings.EMAIL_HOST_USER, from_email=settings.EMAIL_HOST_USER,
                                subject=admin_subject, message=admin_message)
