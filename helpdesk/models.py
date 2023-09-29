from django.db import models
import time
import random
import string


# Create your models here.

def gen_ticket_id():
    # Generate a random string with length 5
    random_str = ''.join(random.choices(string.ascii_letters, k=5))
    # Get the current timestamp
    now = str(int(time.time()))
    return "#" + random_str + now


class TicketSystem(models.Model):
    ticket_id = models.CharField(max_length=20, default=gen_ticket_id, unique=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticket_id

    class Meta:
        verbose_name_plural = "TicketSystem"
