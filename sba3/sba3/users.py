from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# https://docs.djangoproject.com/en/dev/topics/auth/customizing/
class Users(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, blank=False)
    username = models.CharField(max_length=20, blank=False)
    display_name = models.CharField(max_length=45, blank=True)

    USERNAME_FIELD = 'email' # specify unique key
    REQUIRED_FIELDS = ['email', ] # only affects createsuperuser command
    is_active = True

    # Required to override these methods, else throw exception when called
    def get_full_name(self):
    	if display_name == "":
    		return self.username
    	return self.display_name
    def get_short_name(self):
    	return self.username


 class UsersManager(BaseUserManager):
 	def create_user(self):
 		now = timezone.now()