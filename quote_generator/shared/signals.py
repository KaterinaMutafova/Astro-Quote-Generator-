from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from quote_generator.profiles.models import UserProfile
from quote_generator.quotes.models import Quote
from quote_generator.shared.templatetags.my_group_filter import has_group

UserModel = get_user_model()


# Create extended profile  to the user:
@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile(
            user=instance,
        )

        profile.save()


# Add user to the group "Regular user" when the user is created:
@receiver(post_save, sender=UserModel)
def add_regular_user(sender, instance, created, **kwargs):
    if created:
        user = instance
        my_regular_group = Group.objects.get(name='Regular user')
        my_regular_group.user_set.add(user)


# Add user to the group "Special user":
@receiver(post_save, sender=Quote)
def add_special_user(sender, instance, **kwargs):
    my_special_group = Group.objects.get(name='Special user')
    added_by_user = instance.added_by
    quotes_added_by_user = Quote.objects.filter(added_by=added_by_user)
    if len(quotes_added_by_user) >= 3:
        my_special_group.user_set.add(added_by_user)


# Remove user from the group "Special user":
@receiver(post_delete, sender=Quote)
def remove_special_user(sender, instance, **kwargs):
    my_special_group = Group.objects.get(name='Special user')
    added_by_user = instance.added_by
    quotes_added_by_user = Quote.objects.filter(added_by=added_by_user)
    if len(quotes_added_by_user) < 3 and has_group(added_by_user, my_special_group):
        my_special_group.user_set.remove(added_by_user)


# Check if the user has completed all the important fields in the profile:
@receiver(pre_save, sender=UserProfile)
def check_is_complete(sender, instance, **kwargs):
    if instance.first_name and instance.last_name and instance.date_of_birth and instance.image:
        instance.is_complete = True
    else:
        instance.is_complete = False




