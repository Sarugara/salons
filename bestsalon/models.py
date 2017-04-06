# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta
from django.utils.encoding import smart_unicode
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    contact = models.CharField(max_length=250)
    adress = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='users/', default='users/avatar.jpg')

    def __unicode__(self):
        return smart_unicode(self.user)

class City(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return str(self.name.encode('utf-8').strip())

class ServiceCategory(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.cat_name.encode('utf-8').strip())

class Services(models.Model):
    cat = models.ForeignKey(ServiceCategory)
    service_name = models.CharField(max_length=100)

    def __unicode__(self):
        return smart_unicode(self.service_name)


class MyService(models.Model):
    service = models.ForeignKey(Services)
    service_desc = models.CharField(max_length=250)
    service_price = models.CharField(max_length=250)

    def __unicode__(self):
        return smart_unicode(self.service)

class Book(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    service = models.ManyToManyField(Services)
    book = models.TextField(max_length=500)
    date = models.DateTimeField(default=datetime.now() + timedelta(days=1))
    flag = models.IntegerField(default=1)

    def __unicode__(self):
        return smart_unicode(self.book)

class Feedback(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    feedback = models.TextField(max_length=500)

class Photos(models.Model):
    photos = models.ImageField(upload_to='salonsphotos/')

class Salons(models.Model):
    city = models.ForeignKey(City, default=1)
    salon_author = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=250)
    salon_desc = models.CharField(max_length=500)
    salon_contact = models.CharField(max_length=250, null=True)
    salon_site = models.CharField(max_length=100, null=True)
    salon_adress = models.CharField(max_length=100)
    salon_logo = models.ImageField(upload_to='media/', default='media/no.jpg')
    salon_services = models.ManyToManyField(MyService)
    salon_photos = models.ManyToManyField(Photos)
    salon_feedback = models.ManyToManyField(Feedback)
    salon_book = models.ManyToManyField(Book)

    def __str__(self):
        return str(self.name.encode('utf-8').strip())

    def get_absolute_url(self):
        return reverse('salons:detail', kwargs={'pk': self.pk})

class Masters(models.Model):
    salon = models.ForeignKey(Salons)
    master_name = models.CharField(max_length=250)
    master_desc = models.CharField(max_length=500)
    master_logo = models.ImageField(upload_to='masters/', default='masters/noname.jpg')

    def __str__(self):
        return str(self.master_name.encode('utf-8').strip())

class Works(models.Model):
    salon = models.ForeignKey(Salons)
    work_service = models.ManyToManyField(Services)
    work_desc = models.CharField(max_length=250)
    work_logo = models.ImageField(upload_to='works/')
    work_like = models.IntegerField(default=0)
    wholikeit = models.ManyToManyField(User)

    def __str__(self):
        return str(self.work_desc.encode('utf-8').strip())

class ValueOfSalon(models.Model):
    salon = models.ForeignKey(Salons)
    servicevalue = models.IntegerField(default=0)
    workvalue = models.IntegerField(default=0)
    sumvalue = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    whovalueit = models.ManyToManyField(User)

    def __str__(self):
        return str(self.salon)



















class SelfMaster(models.Model):
    master_author = models.ForeignKey(User, blank=True, null=True)
    master_services = models.ManyToManyField(MyService)
    master_feedback = models.ManyToManyField(Feedback)
    master_book = models.ManyToManyField(Book)
    city = models.ForeignKey(City, default=1)
    wholoveit = models.ManyToManyField(User,  related_name='who_love_this_master', blank=True)

    def __unicode__(self):
        return smart_unicode(self.master_author)


class SelfServiceCategory(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_desc = models.CharField(max_length=250)
    cat_logo = models.ImageField(upload_to='servicecat/')

    def __unicode__(self):
        return smart_unicode(self.cat_name)

class SelfWorks(models.Model):
    master = models.ForeignKey(SelfMaster)
    work_service = models.ForeignKey(Services, default=0)
    work_desc = models.CharField(max_length=250)
    work_logo = models.ImageField(upload_to='works/')
    work_like =  models.IntegerField(default=0)
    wholikeit = models.ManyToManyField(User)

    def __unicode__(self):
        return smart_unicode(self.work_desc)

class SelfValueOfMaster(models.Model):
    master = models.ForeignKey(SelfMaster)
    servicevalue = models.IntegerField(default=0)
    workvalue = models.IntegerField(default=0)
    sumvalue = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    whovalueit = models.ManyToManyField(User)

    def __unicode__(self):
        return smart_unicode(self.master)


class FavSalons(models.Model):
    salon = models.ForeignKey(Salons)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return smart_unicode(self.user)

class FavMasters(models.Model):
    master = models.ForeignKey(SelfMaster)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return smart_unicode(self.user)














