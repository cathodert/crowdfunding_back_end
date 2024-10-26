from django.db import models
from django.contrib.auth import get_user_model



class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class Band(models.Model):
    name = models.CharField(max_length=150, unique=True)
    country = models.CharField(max_length=50)
    description = models.TextField()
    cover_image = models.URLField()
    website = models.URLField()
    genre = models.ManyToManyField(Genre)

# NOTE This indicates if band is still together / performing. False would not be able to create a tour but would be retained in database. When band created this defaults to True (not visible on form?). Owner can update to False at later point.
    is_current = models.BooleanField(default=True)

# NOTE currently band will only have one owner and if owner is deleted the band will be deleted. For future - more than one user can be associated with a band (band members) and any band member can edit details of band once created. on_delete should be PROTECT as do not want to delete the band if the user is deleted. 
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)


# TODO This is automatically updated where open project is associated with band.
# I would like front-end for band page to display links to current (and previous) tours. Need to work out how to do this.
    # upcoming_tour = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.name

#  TODO Add rules around deletion.
    # def delete(self):
    #     self.active = False
    #     self.save()

class Tour(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
# TODO update goal to max value e.g. 50,000
    goal = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    
# TODO add rule that tour owner needs to be member of band.
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE)
    
    band = models.ForeignKey(
       'Band',
        on_delete=models.CASCADE,
        related_name='all_tours'
    )
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.title


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    band = models.ForeignKey(
        'Band',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    tour = models.ForeignKey(
        'Tour',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )
