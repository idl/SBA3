import re
from django.utils import timezone as tz
from django.db import models
from django.core import validators
from django.contrib.auth.hashers import (
    check_password, make_password, is_password_usable)
from django.contrib.auth.models import BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
	def _create_user(self, username, email, password, is_superuser=False):
		if not username:
			raise ValueError("Users must have a username.")
		elif not email:
			raise ValueError("Users must have an email.")
		elif not password:
			raise ValueError("Users must have a password.")
		email = self.normalize_email(email)
		user = self.model(    
                            username=username,
                            email=email,
                            is_active=True,
                            is_superuser=is_superuser, 
                            last_login=tz.now(),
                            date_joined=tz.now()
                          )
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, email, password):
		return self._create_user(username, email, password)

	def create_superuser(self, username, email, password):
	    return self._create_user(username, email, password, is_superuser=True)


class AbstractBaseUser(models.Model):
    password = models.CharField('password', max_length=128)
    last_login = models.DateTimeField('last login', default=tz.now)

    is_active = True

    REQUIRED_FIELDS = []

    class Meta:
        abstract = True

    def get_username(self):
        "Return the identifying username for this User"
        return getattr(self, self.USERNAME_FIELD)

    def __str__(self):
        return self.get_username()

    def natural_key(self):
        return (self.get_username(),)

    def is_anonymous(self):
        """
        Always returns False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    def set_unusable_password(self):
        # Sets a value that will never be a valid hash
        self.password = make_password(None)

    def has_usable_password(self):
        return is_password_usable(self.password)

    def get_full_name(self):
        raise NotImplementedError()

    def get_short_name(self):
        raise NotImplementedError()


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username, password and email are required. Other fields are optional.
    """
    username = models.CharField('username', max_length=30, unique=True, blank=False,
        help_text='Required. 30 characters or fewer. Letters, numbers and '
                    '@/./+/-/_ characters',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid username.', 'invalid')
        ])
    email = models.EmailField('email address', unique=True, blank=False)
    display_name = models.CharField('display name', max_length=30, blank=True, default='')
    date_joined = models.DateTimeField('date joined', default=tz.now())
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = True

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.username)

    def get_full_name(self):
    	if self.display_name != '':
    		return self.display_name
    	return self.username.capitalize()

    def get_short_name(self):
        return self.username

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])


class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


# class AnonymousUser(object):
#     id = None
#     pk = None
#     username = ''
#     is_staff = False
#     is_active = False
#     is_superuser = False
#     _groups = EmptyManager(Group)
#     _user_permissions = EmptyManager(Permission)

#     def __init__(self):
#         pass

#     def __str__(self):
#         return 'AnonymousUser'

#     def __eq__(self, other):
#         return isinstance(other, self.__class__)

#     def __ne__(self, other):
#         return not self.__eq__(other)

#     def __hash__(self):
#         return 1  # instances always return the same hash value

#     def save(self):
#         raise NotImplementedError

#     def delete(self):
#         raise NotImplementedError

#     def set_password(self, raw_password):
#         raise NotImplementedError

#     def check_password(self, raw_password):
#         raise NotImplementedError

#     def _get_groups(self):
#         return self._groups
#     groups = property(_get_groups)

#     def _get_user_permissions(self):
#         return self._user_permissions
#     user_permissions = property(_get_user_permissions)

#     def get_group_permissions(self, obj=None):
#         return set()

#     def get_all_permissions(self, obj=None):
#         return _user_get_all_permissions(self, obj=obj)

#     def has_perm(self, perm, obj=None):
#         return _user_has_perm(self, perm, obj=obj)

#     def has_perms(self, perm_list, obj=None):
#         for perm in perm_list:
#             if not self.has_perm(perm, obj):
#                 return False
#         return True

#     def has_module_perms(self, module):
#         return _user_has_module_perms(self, module)

#     def is_anonymous(self):
#         return True

#     def is_authenticated(self):
#         return False

