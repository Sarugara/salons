# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError, CharField, EmailField
from .models import Salons, Masters, Works, Services, \
                    UserProfile, \
                    ValueOfSalon, SelfMaster, SelfWorks, \
                    MyService, SelfValueOfMaster, \
                    FavMasters, FavSalons, Photos, Feedback, Book, City, ServiceCategory
from django.contrib.auth.models import User
from django.db.models import Q

class SalonsSerializer(ModelSerializer):
    class Meta:
        model = Salons
        fields = ('pk', 'city', 'salon_author', 'salon_logo', 'salon_services', 'name', 'salon_desc', 'salon_contact', 'salon_adress', 'salon_site', 'salon_photos', 'salon_feedback', 'salon_book')


class SalonsFavSerializer(ModelSerializer):
    class Meta:
        model = Salons
        fields = ('pk', 'city', 'salon_author', 'name', 'salon_desc', 'salon_logo', 'salon_contact')

class EditSalonsSerializer(ModelSerializer):
    class Meta:
        model = Salons
        fields = ('pk', 'city', 'name', 'salon_desc', 'salon_contact', 'salon_adress', 'salon_site')

class AllSalonsSerializer(ModelSerializer):
    class Meta:
        model = Salons
        fields = ('pk', 'city', 'salon_author', 'salon_logo', 'name', 'salon_desc', 'salon_adress', 'salon_photos', 'salon_feedback', 'salon_book')

class AllCreateSalonsSerializer(ModelSerializer):
    class Meta:
        model = Salons
        fields = ('pk', 'city', 'salon_author', 'salon_logo', 'name', 'salon_desc', 'salon_contact', 'salon_adress')


class ApiCitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ('pk', 'name')


class SalonBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk', 'user', 'service', 'book', 'date', 'flag')


class BookEditSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk', 'flag')


class PutSalonBookSerializer(ModelSerializer):
    class Meta:
        model = Salons
        fields = ('pk', 'salon_book')

class SalonFeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('pk', 'user', 'feedback')

class MasterFeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('pk', 'user', 'feedback')


class GetSalonServiceSerializer(ModelSerializer):
    class Meta:
        model = Salons
        fields = ('pk', 'city', 'salon_services')

class PutSalonFeedbackSerializer(ModelSerializer):
    class Meta:
        model = Salons
        fields = ('pk', 'salon_feedback')

class SalonPhotosSerializer(ModelSerializer):
    class Meta:
        model = Photos
        fields = ('pk', 'photos')

class PutSalonPhotosSerializer(ModelSerializer):
    class Meta:
        model = Salons
        fields = ('pk', 'salon_photos')

class PostSalonImageSerializer(ModelSerializer):
    salon_logo = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Salons
        fields = ('pk', 'salon_logo')






class SalonMastersSerializer(ModelSerializer):
    class Meta:
        model = Masters
        fields = ('pk', 'salon', 'master_name', 'master_desc', 'master_logo')

class SalonWorksSerializer(ModelSerializer):
    class Meta:
        model = Works
        fields = ('pk', 'work_service', 'salon', 'work_desc', 'work_logo')
class SalonWorksWithLikeSerializer(ModelSerializer):
    class Meta:
        model = Works
        fields = ('pk', 'work_service', 'salon', 'work_desc', 'work_logo', 'work_like', 'wholikeit')


class SalonLikeSerializer(ModelSerializer):
    class Meta:
        model = Works
        fields = ('pk', 'work_like', 'wholikeit')

class SelfWorkLikeSerializer(ModelSerializer):
    class Meta:
        model = Works
        fields = ('pk', 'work_like', 'wholikeit')

class EditSalonServicesSerializer(ModelSerializer):
    class Meta:
        model = Salons
        fields = ('pk', 'salon_services')


class SalonServicesSerializer(ModelSerializer):
    class Meta:
        model = MyService
        fields = ('pk', 'service', 'service_desc', 'service_price')

class GetSalonCatServicesSerializer(ModelSerializer):
    class Meta:
        model = Services
        fields = ('pk', 'cat', 'service_name')
class GetGlobeCatServicesSerializer(ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ('pk', 'cat_name')





class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'first_name', 'last_name', 'email')

class EditUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'first_name', 'last_name', 'email')

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('pk', 'user', 'contact', 'adress', 'avatar')

class PostUserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('pk', 'user')

class UserLogoSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('pk', 'user', 'avatar')




class CreateUserSerializer(ModelSerializer):
    repassword = CharField(label="Confirm password")


    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'repassword')
        extra_kwargs = {"password":
                            {"write_only": True}
                        }


    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("Пользователь с таким email уже существует!")
        return data

    def validate_repassword(self, value):
        data = self.get_initial()
        password = data.get("password")
        repassword = value
        if password != repassword:
            raise ValidationError("Пароли не совпадают")


    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data





class LoginUserSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(required=False, allow_blank=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'token')
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        user_obj=None
        email = data.get('email', None)
        username = data.get('username', None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("Логин и email необзодимы для входа")
        user = User.objects.filter(
             Q(email=email) |
             Q(username=username)
         ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Неверный логин или email")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Неверный пароль")

        data["token"] = "Some random token"
        return data

class AccountSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

class ValueOfSalonSerializer(ModelSerializer):
    class Meta:
        model = ValueOfSalon
        fields = ('pk', 'whovalueit', 'salon', 'servicevalue', 'workvalue', 'sumvalue', 'count')






class SelfMasterSerializer(ModelSerializer):
    class Meta:
        model = SelfMaster
        fields = ('pk', 'city', 'wholoveit', 'master_feedback', 'master_author')


class JustSelfMasterSerializer(ModelSerializer):
    class Meta:
        model = SelfMaster
        fields = ('pk', 'city', 'wholoveit', 'master_author')



class SalonCatServicesSerializer(ModelSerializer):
    class Meta:
        model = SelfMaster
        fields = ('pk', 'city', 'wholoveit', 'master_author')

class SelfMasterServicesSerializer(ModelSerializer):
    class Meta:
        model = SelfMaster
        fields = ('pk', 'city', 'master_author', 'master_services')

class SelfServiceSerializer(ModelSerializer):
    class Meta:
        model = SelfMaster
        fields = ('pk', 'master_services')

class SelfWorksSerializer(ModelSerializer):
    class Meta:
        model = SelfWorks
        fields = ('pk', 'work_service', 'master', 'work_desc', 'work_logo')

class SelfWorksWithLikeSerializer(ModelSerializer):
    class Meta:
        model = SelfWorks
        fields = ('pk', 'work_service', 'master', 'work_desc', 'work_logo', 'work_like', 'wholikeit')

class SelfLikeSerializer(ModelSerializer):
    class Meta:
        model = SelfWorks
        fields = ('pk', 'work_like')

class SelfValueOfMasterSerializer(ModelSerializer):
    class Meta:
        model = SelfValueOfMaster
        fields = ('pk', 'whovalueit', 'master', 'servicevalue', 'workvalue', 'sumvalue', 'count')

class SelfWhoLoveSerializer(ModelSerializer):
    class Meta:
        model = SelfMaster
        fields = ('pk', 'wholoveit')


class PutMasterFeedbackSerializer(ModelSerializer):
    class Meta:
        model = SelfMaster
        fields = ('pk', 'master_feedback')




class FavSalonsSerializer(ModelSerializer):
    class Meta:
        model = FavSalons
        fields = ('pk', 'salon', 'user')

class FavMastersSerializer(ModelSerializer):
    class Meta:
        model = FavMasters
        fields = ('pk', 'master', 'user')



