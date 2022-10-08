from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class AppUser(models.Model):
    qr_photo = models.FileField(upload_to='account_files/profile_photos/', blank=True, default="default_files/default_face.jpg")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(default="candidate",max_length=10)

    cprofile_status = models.BooleanField(default=False)
    cv = models.FileField(upload_to='account_files/profile_photos/', blank=True, default="default_files/default_face.jpg")
    profile_photo = models.FileField(upload_to='account_files/profile_photos/', blank=True, default="default_files/default_face.jpg")
    address = models.TextField(default=" ")
    country = models.CharField(default=" ",max_length=100)
    phone_no = models.CharField(default=" ",max_length=15)
    age = models.IntegerField(default=18)
    gender = models.CharField(default=" ",max_length=10)

    #socials
    facebook_link = models.CharField(default="#",max_length=100)
    twitter_link = models.CharField(default="#",max_length=100)
    instagram_link = models.CharField(default="#",max_length=100)
    whatsapp_link = models.CharField(default="#",max_length=100)
    github_link = models.CharField(default="#",max_length=100)


    #recruiters
    agency_name = models.CharField(default="",max_length=30, null=True)
    rank = models.CharField(default="1",max_length=30, null=True)
    ranks = models.CharField(default="1",max_length=30, null=True)
    rankers = models.CharField(default="1",max_length=30, null=True)
    charge = models.CharField(default="0",max_length=30, null=True)
    bio = models.TextField(default="This agency have not updated their bio..")
    agency_logo = models.FileField(upload_to='account_files/profile_photos/', blank=True, default="default_files/default_face.jpg")

    

    otp_code = models.CharField(default="none",max_length=10)
    
    ec_status = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    
    passphrase0 = models.CharField(default="none",max_length=10)
    passphrase1 = models.CharField(default="none",max_length=10)
    passphrase2 = models.CharField(default="none",max_length=10)
    passphrase3 = models.CharField(default="none",max_length=10)
    passphrase4 = models.CharField(default="none",max_length=10)
    passphrase5 = models.CharField(default="none",max_length=10)
    passphrase6 = models.CharField(default="none",max_length=10)
    passphrase7 = models.CharField(default="none",max_length=10)
    passphrase8 = models.CharField(default="none",max_length=10)
    passphrase9 = models.CharField(default="none",max_length=10)
    passphrase10 = models.CharField(default="none",max_length=10)
    passphrase11 = models.CharField(default="none",max_length=10)
    
    #wallet shit
    wallet_address = models.CharField(default="null",max_length=100)
    wallet_key = models.CharField(default="null",max_length=100)
    
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username