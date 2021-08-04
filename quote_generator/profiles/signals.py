from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from quote_generator.profiles.models import UserProfile


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile(
            user=instance,
        )

        profile.save()

@receiver(pre_save, sender=UserProfile)
def check_is_complete(sender, instance, **kwargs):
    if instance.first_name and instance.last_name and instance.date_of_birth and instance.profile_image:
        instance.is_complete = True

