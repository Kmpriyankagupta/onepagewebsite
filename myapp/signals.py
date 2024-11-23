from django.db.models.signals import *
from .models import *
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils.timezone import now
from .models import UserLog
from django.contrib.sessions.models import Session
from django.utils.timezone import localtime

@receiver(post_save, sender=Author)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(author=instance)
        instance.profile.save()


def get_client_ip(request):
    """Retrieve the client's IP address."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ip_address = get_client_ip(request)
    UserLog.objects.create(user=user, action='login', ip_address=ip_address, timestamp=now())
    print(f"User {user.username} logged in at {localtime(now())}")


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    ip_address = get_client_ip(request)
    UserLog.objects.create(user=user, action='logout', ip_address=ip_address, timestamp=now())
    print(f"User {user.username} logged out at {localtime(now())}")

# @receiver(pre_init, sender=cloths)
# def modify_init_args(sender, args, kwargs, **extra):
#     if 'price' not in kwargs:
#         print("Setting default price in pre_init")
#         kwargs['price'] = 100.0  # Default price if not provided

# @receiver(post_init, sender=cloths)
# def log_model_initialization(sender, instance, **kwargs):
#     """Log instance details after initialization."""
#     print(f"Post-init: A Product instance was created - Name: {instance.name}, Price: {instance.price}")

