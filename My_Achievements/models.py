from django.conf import settings
from django.db import models


class Theme(models.Model):
    name_theme = models.CharField(max_length=255)
    max_scores = models.DecimalField(decimal_places=5, max_digits=10)


class UserSite(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student_card = models.IntegerField()
    name_user = models.CharField(max_length=255)
    surname_user = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    year = models.IntegerField()
    group = models.CharField(max_length=10)


class Achievement(models.Model):
    name_themes = models.ForeignKey(Theme, on_delete=models.PROTECT)
    user = models.ForeignKey(UserSite, on_delete=models.PROTECT)
    path_to_doc = models.TextField()
    scores = models.DecimalField(decimal_places=5, max_digits=10)
    confirmed = models.BooleanField()


class Role(models.Model):
    name_role = models.CharField(max_length=255)


class Access(models.Model):
    name_theme = models.ForeignKey(Theme, on_delete=models.PROTECT)
    name_role = models.ForeignKey(Role, on_delete=models.PROTECT)