from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
class UserProfileInfo(models.Model):
    CRICKET = 'Cr'
    FOOTBALL = 'Fb'
    HOCKEY = 'Ho'
    BADMINTON = 'Bm'
    VOLLEYBALL = 'Vb'
    SPORT_CHOICES = [
        (CRICKET, 'Cricket'),
        (FOOTBALL, 'Football'),
        (HOCKEY, 'Hockey'),
        (BADMINTON, 'Badminton'),
        (VOLLEYBALL, 'Volleyball'),
    ]
    INDIA = 'Ind'
    JAPAN = 'Jpn'
    CHINA = 'Chn'
    USA = 'Usa'
    RUSSIA = 'Rs'
    COUNTRY_CHOICES = [
        (INDIA,"India"),
        (JAPAN,"Japan"),
        (CHINA,"China"),
        (USA,"Usa"),
        (RUSSIA,"Russia")
    ]
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    portofolio_site = models.URLField(blank='False')
    country = models.CharField(max_length = 32,choices = COUNTRY_CHOICES,)
    sport = models.CharField(max_length = 32,choices = SPORT_CHOICES,)
    profile_pic = models.ImageField(blank='False',upload_to = 'profile_pics')
    def __str__(self):
        return self.user.username
class Result_Men(models.Model):
    CRICKET = 'Cr'
    FOOTBALL = 'Fb'
    HOCKEY = 'Ho'
    BADMINTON = 'Bm'
    VOLLEYBALL = 'Vb'
    SPORT_CHOICES = [
        (CRICKET, 'Cricket'),
        (FOOTBALL, 'Football'),
        (HOCKEY, 'Hockey'),
        (BADMINTON, 'Badminton'),
        (VOLLEYBALL, 'Volleyball'),
    ]
    sport = models.CharField(max_length = 32,choices = SPORT_CHOICES,null=False, blank=False,default='',unique=True)
    gold_medal = models.ForeignKey(User,on_delete = models.CASCADE,related_name="gold_men",null=True,blank=True,default = 'gold')
    silver_medal = models.ForeignKey(User,on_delete = models.CASCADE,related_name="silver_men",null=True,blank=True)
    bronze_medal = models.ForeignKey(User,on_delete = models.CASCADE,related_name="bronze_men",null=True,blank=True)
    def __str__(self):
        return self.sport
    class Meta:
        unique_together = ('gold_medal','silver_medal','bronze_medal',)
class Result_Women(models.Model):
    CRICKET = 'Cr'
    FOOTBALL = 'Fb'
    HOCKEY = 'Ho'
    BADMINTON = 'Bm'
    VOLLEYBALL = 'Vb'
    SPORT_CHOICES = [
        (CRICKET, 'Cricket'),
        (FOOTBALL, 'Football'),
        (HOCKEY, 'Hockey'),
        (BADMINTON, 'Badminton'),
        (VOLLEYBALL, 'Volleyball'),
    ]
    sport = models.CharField(max_length = 32,choices = SPORT_CHOICES,null=False, blank=False,default='',unique=True)
    gold_medal = models.ForeignKey(User,on_delete = models.CASCADE,related_name="gold_women",null=True,blank=True)
    silver_medal = models.ForeignKey(User,on_delete = models.CASCADE,related_name="silver_women",null=True,blank=True)
    bronze_medal = models.ForeignKey(User,on_delete = models.CASCADE,related_name="bronze_women",null=True,blank=True)
    def __str__(self):
        return self.sport
    class Meta:
        unique_together = ('gold_medal','silver_medal','bronze_medal',)
class Medals(models.Model):
    INDIA = 'Ind'
    JAPAN = 'Jpn'
    CHINA = 'Chn'
    USA = 'Usa'
    RUSSIA = 'Rs'
    COUNTRY_CHOICES = [
        (INDIA,"India"),
        (JAPAN,"Japan"),
        (CHINA,"China"),
        (USA,"Usa"),
        (RUSSIA,"Russia")
    ]
    country = models.CharField(max_length = 32,choices = COUNTRY_CHOICES,null=False, blank=False,default='',unique=True)
    gold_medal = models.PositiveIntegerField(default=0)
    silver_medal = models.PositiveIntegerField(default=0)
    bronze_medal = models.PositiveIntegerField(default=0)
    total_medals = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['gold_medal','silver_medal','bronze_medal','total_medals']
    def __str__(self):
        return self.country
