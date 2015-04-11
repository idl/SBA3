# import re
# from django.utils import timezone as tz
# from django.db import models
# from django.core import validators
# from django.contrib.auth.hashers import (
#   check_password, make_password, is_password_usable)
# from django.contrib.auth.models import BaseUserManager, PermissionsMixin

# class UserManager(BaseUserManager):
#   def _create_user(self, email, password, is_superuser=False, school_id=None):
#     if not email:
#       raise ValueError("Users must have an email.")
#     elif not password:
#       raise ValueError("Users must have a password.")
#     if is_superuser:
#       school_id = None
#     email = self.normalize_email(email)
#     user = self.model(
#         email=email,
#         is_active=True,
#         is_superuser=is_superuser,
#         last_login=tz.now(),
#         date_joined=tz.now(),
#         school_id=school_id
#         )
#     user.set_password(password)
#     user.save(using=self._db)
#     return user

#   def create_user(self, email, password, school_id):
#     return self._create_user(email, password, school_id=school_id)

#   def create_superuser(self, email, password):
#     return self._create_user(email, password, is_superuser=True)


# class AbstractBaseUser(models.Model):
#   password = models.CharField('password', max_length=128)
#   last_login = models.DateTimeField('last login', default=tz.now())

#   is_active = True

#   REQUIRED_FIELDS = []

#   class Meta:
#     abstract = True

#   def get_username(self):
#     "Return the identifying username for this User"
#     return getattr(self, self.USERNAME_FIELD)

#   def __str__(self):
#     return self.get_username()

#   def natural_key(self):
#     return (self.get_username(),)

#   def is_anonymous(self):
#     """
#     Always returns False. This is a way of comparing User objects to
#     anonymous users.
#     """
#     return False

#   def is_authenticated(self):
#     """
#     Always return True. This is a way to tell if the user has been
#     authenticated in templates.
#     """
#     return True

#   def set_password(self, raw_password):
#     self.password = make_password(raw_password)

#   def check_password(self, raw_password):
#     """
#     Returns a boolean of whether the raw_password was correct. Handles
#     hashing formats behind the scenes.
#     """
#     def setter(raw_password):
#       self.set_password(raw_password)
#       self.save(update_fields=["password"])
#     return check_password(raw_password, self.password, setter)

#   def set_unusable_password(self):
#     # Sets a value that will never be a valid hash
#     self.password = make_password(None)

#   def has_usable_password(self):
#     return is_password_usable(self.password)

#   def get_full_name(self):
#     raise NotImplementedError()

#   def get_short_name(self):
#     raise NotImplementedError()


# class AbstractUser(AbstractBaseUser, PermissionsMixin):
#   """
#   An abstract base class implementing a fully featured User model with
#   admin-compliant permissions.

#   Username, password and email are required. Other fields are optional.
#   """
#   email = models.EmailField('email address', unique=True, blank=False)
#   date_joined = models.DateTimeField('date joined', default=tz.now())
#   is_active = models.BooleanField(default=True)
#   # if school_id is Null then it has to be a superadmin, not school admin
#   school_id = models.CharField('school id', default=None, max_length=30, null=True)

#   objects = UserManager()

#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = []

#   class Meta:
#     verbose_name = 'user'
#     verbose_name_plural = 'users'
#     abstract = True

#   def get_absolute_url(self):
#     return "/users/%s/" % urlquote(self.username)

#   def get_full_name(self):
#     if self.display_name != '':
#       return self.display_name
#     return self.username.capitalize()

#   def get_short_name(self):
#     return self.username

#   def email_user(self, subject, message, from_email=None):
#     """
#     Sends an email to this User.
#     """
#     send_mail(subject, message, from_email, [self.email])


# class User(AbstractUser):
#   class Meta(AbstractUser.Meta):
#     swappable = 'AUTH_USER_MODEL'
