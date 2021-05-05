from django.db import models
from django.utils.timezone import now
# Create your models here.


class User(models.Model):
    fname = models.CharField(max_length=20, null=False)
    mname = models.CharField(max_length=20, default='', null=True)
    lname = models.CharField(max_length=20, default='', null=True)
    email = models.EmailField(max_length=30, default='', null=False)
    gender = models.CharField(max_length=5, default='', null=False)
    phoneno = models.CharField(max_length=10, default='', null=False)
    password = models.CharField(max_length=15, default='', null=False)
    status = models.CharField(max_length=1, default='0', null=False)
    queasked = models.IntegerField(default=0)
    ansgive = models.IntegerField(default=0)
    imgpicture = models.FileField(blank=True)


class Question(models.Model):
    name = models.CharField(max_length=25, null=False, default='')
    length = models.IntegerField(default=0)
    question = models.CharField(max_length=250, null=False, default='')
    topic = models.CharField(max_length=20, null=False, default='')
    email = models.EmailField(max_length=30, default='', null=False)
    wquestion = models.CharField(max_length=1,  default='0', null=False)
    totalans = models.IntegerField(default=0)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=False, default=now)


class Report(models.Model):
    helper = models.CharField(max_length=50, null=False, default='')
    email = models.CharField(max_length=30, null=False, default='')
    funame = models.CharField(max_length=30, null=False)
    describ = models.CharField(max_length=100, null=False)


class Answer(models.Model):
    answer = models.CharField(max_length=1000, null=False, default='')
    name = models.CharField(max_length=25, null=False, default='')
    idanswer = models.IntegerField(default=0)
    email = models.EmailField(max_length=30, default='', null=False)
    question = models.CharField(max_length=250, null=False, default='')
    asked = models.CharField(max_length=50, null=False, default='')
    upvotes = models.IntegerField(default=0)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=False, default=now)


class Review(models.Model):
    rid = models.IntegerField(default=0)
    answerid = models.IntegerField(default=0)


class Delete(models.Model):
    reason = models.CharField(max_length=300, null=True, default='')
    email = models.CharField(max_length=30, null=False, default='')