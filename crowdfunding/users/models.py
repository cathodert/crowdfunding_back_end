from django.db import models
from django.contrib.auth.models import AbstractUser

    

class CustomUser(AbstractUser):

    is_band = models.BooleanField(
        "band member",
        default=False,
        help_text=("Designates if user is a member of a band and therefore able to create bands and tours"),
    )

    class Supporter:
        is_band = False

    class BandMember:
        is_band = True


    def __str__(self):
        return self.username




    

