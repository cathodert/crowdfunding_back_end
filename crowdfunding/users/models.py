from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

class CustomUser(AbstractUser):
    SUPPORTER = "SU"
    BAND_MEMBER = "BM"
    USER_TYPE_CHOICES = {
        SUPPORTER: "Supporter",
        BAND_MEMBER: "Band member",
        }

# common fields
    email = models.EmailField(unique=True, blank=False)
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    user_type = models.CharField(
        max_length=2,
        choices=USER_TYPE_CHOICES,
        blank=False)
    
    # TODO removed genres from sprint project as had issues with Not Null and couldn't work it out
    # user_genres = models.ForeignKey(
    #     # models.ManyToManyField(
    #     'projects.Genre', 
    #     blank=True,
    #     # null=True,
    #     # on_delete=models.CASCADE
    #     )

 # TODO removed genres from sprint project as had issues with Not Null and couldn't work it out
# fields unique to band member - only visible / editable after user profile has been created
    # users_bands = models.ForeignKey(
    #     'projects.Band', 
    #     blank=True,
    #     null=True,
    #     on_delete=models.CASCADE
    #     )

    def supporter(self):
        return self.user_type in{self.SUPPORTER}
    
    # TODO work out how to set permissions for band member
    def band_member(self):
        # class Meta:
        #     permissions = Permission.objects.create(
        #         new_band = "can_create_band",
        #         new_tour = "can_create_tour"
        #     )

        return self.user_type in {self.BAND_MEMBER}



    def __str__(self):
        return self.username




    

