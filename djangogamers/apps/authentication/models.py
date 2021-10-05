from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework_simplejwt.tokens import RefreshToken

from djangogamers.apps.core.models import CommonFieldsMixin


class User(AbstractUser, CommonFieldsMixin):
    """ Base class for all users """
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)

    class Types(models.TextChoices):
        """ User Types """
        GAMER = "GAMER", "Gamer"
        DEVELOPER = "DEVELOPER", "Developer"
        PUBLISHER = "PUBLISHER", "Publisher"
        STAFFMEMBER = "STAFFMEMBER", "StaffMember"
        ADMIN = "ADMIN", "Admin"

    base_type = Types.ADMIN
    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=base_type)
    email = models.CharField(_("email of User"), unique=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = self.base_type
            return super().save(*args, kwargs)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


""" ========================= Proxy Model Managers =================== """


class GamerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.BRAND)


class DeveloperManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.BUYER)


class PublisherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.COURIER)


class StaffManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.STAFFMEMBER)


""" ========================== Proxy Models ============================== """


class Gamer(User):
    """Class to create Brand Object & Associated attributes """
    base_type = User.Types.GAMER
    objects = GamerManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.GAMER
            self.set_password(self.password)
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True
        ordering = ['-created_at', '-updated_at']


class Developer(User):
    """ class to create buyer object & associated attributes """
    base_type = User.Types.DEVELOPER
    objects = DeveloperManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.DEVELOPER
            self.set_password(self.password)
        return super().save(*args, **kwargs)

    class Meta:
        proxy = True
        ordering = ['-created_at', '-updated_at']


class Publisher(User):
    """ Class to create courier object & associated attributes """
    base_type = User.Types.PUBLISHER
    objects = PublisherManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.PUBLISHER
            self.set_password(self.password)
        return super().save(*args, **kwargs)


class StaffMember(User):
    """ Class to create StaffMember object & associated attributes """
    base_type = User.Types.STAFFMEMBER
    objects = StaffManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.STAFFMEMBER
            self.set_password(self.password)
        return super().save(*args, **kwargs)


@receiver(post_save, sender=Publisher)
@receiver(post_save, sender=StaffMember)
@receiver(post_save, sender=Gamer)
@receiver(post_save, sender=Developer)
def create_user_profile(sender, instance, created, **kwargs):
    from djangogamers.apps.profiles.models import Profile
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Publisher)
@receiver(post_save, sender=StaffMember)
@receiver(post_save, sender=Gamer)
@receiver(post_save, sender=Developer)
def create_user_profile(sender, instance, **kwargs):
    instance.profile.save()
