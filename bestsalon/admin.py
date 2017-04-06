# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Salons, Masters, Works, Services, ServiceCategory, \
                    UserProfile, SelfMaster, Photos, Feedback, Book, \
                    SelfWorks, MyService, City, FavMasters, SelfValueOfMaster, \
                    ValueOfSalon

# Register your models here.
admin.site.register(Salons)
admin.site.register(Masters)
admin.site.register(Works)
admin.site.register(ServiceCategory)
admin.site.register(Services)
admin.site.register(SelfMaster)
admin.site.register(Photos)
admin.site.register(Feedback)
admin.site.register(Book)
admin.site.register(SelfWorks)
admin.site.register(MyService)
admin.site.register(City)
admin.site.register(FavMasters)
admin.site.register(SelfValueOfMaster)
admin.site.register(ValueOfSalon)






class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)


# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)