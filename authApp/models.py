from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
#from shortuuid.django_fields import ShortUUIDField



# choices to be used by the gender field
GENDER = (
    ("male","Male"),
    ("female","Female")
)

# choices for relationship status
RELATIONSHIP = (
    ("single","Single"),
    ("married","married"),
    ("inlove","In Love"),
)

WHO_CAN_SEE_MY_FRIENDS = (
    ("Only Me","Only Me"),
    ("Everyone","Everyone"),
)


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=250)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=150)
    gender = models.CharField(max_length=100 , choices=GENDER)

    otp = models.CharField(max_length=10,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user.id, ext)
    return 'user_{0}/{1}'.format(instance.user.id,  filename)
    
# user profile. Profile and User model are linked via a 1 to 1 relationship
class Profile(models.Model):
    pid = models.CharField(max_length=30)
    full_name = models.CharField(max_length=250,null=True,blank=True)
    gender = models.CharField(max_length=100,choices=GENDER)
    phone = models.CharField(max_length=200,null=True , blank = True)
    bio = models.CharField(max_length=250 , null = True , blank= True)
    about_me = models.TextField(null=True , blank = True)
    image = models.ImageField()
    cover_image = models.ImageField()
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    relationship = models.CharField(max_length=100, choices=RELATIONSHIP, null=True, blank=True, default="single")
    friends_visibility = models.CharField(max_length=100, choices=WHO_CAN_SEE_MY_FRIENDS, null=True, blank=True, default="Everyone")
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    working_at = models.CharField(max_length=1000, null=True, blank=True)
    instagram = models.URLField(default="https://instagram.com/", null=True, blank=True)
    whatsApp = models.CharField(default="+1207-239-0270", max_length=100, blank=True, null=True)
    verified = models.BooleanField(default=False)
    followers = models.ManyToManyField(User, blank=True, related_name="followers")
    followings = models.ManyToManyField(User, blank=True, related_name="followings")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")
    #groups = models.ManyToManyField("mainApp.Group", blank=True, related_name="groups")
    #pages = models.ManyToManyField("mainApp.Page", blank=True, related_name="pages")
    blocked = models.ManyToManyField(User, blank=True, related_name="blocked")
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)




