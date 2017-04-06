import json
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.views.generic import View
from .models import Salons, Masters, Works, MyService, ServiceCategory, UserProfile, User, ValueOfSalon, \
                    SelfMaster, SelfWorks, SelfValueOfMaster, FavSalons, FavMasters, Photos, Feedback, Book, \
                    Services, City
from django.contrib.auth.models import User
from .forms import UserForm, LoginForm, SalonsForm
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect
from .serializers import SalonsSerializer, AllSalonsSerializer, PostSalonImageSerializer, \
                            SalonMastersSerializer, SalonWorksSerializer, \
                            SalonServicesSerializer, SalonCatServicesSerializer, \
                            UserProfileSerializer, UserSerializer, UserLogoSerializer, CreateUserSerializer, \
                            LoginUserSerializer, AccountSerializer, PostUserProfileSerializer, EditUserSerializer, ValueOfSalonSerializer, \
                            SelfMasterSerializer, SelfWorksSerializer, SelfValueOfMasterSerializer, SelfLikeSerializer, \
                            FavSalonsSerializer, FavMastersSerializer, SalonsFavSerializer, SalonLikeSerializer, SalonWorksWithLikeSerializer, \
                            SelfWorksWithLikeSerializer, SelfWorkLikeSerializer, SalonPhotosSerializer, PutSalonPhotosSerializer, \
                            SalonFeedbackSerializer, PutSalonFeedbackSerializer, SalonBookSerializer, PutSalonBookSerializer, BookEditSerializer, \
                            AllCreateSalonsSerializer, SelfServiceSerializer, SelfMasterServicesSerializer, EditSalonServicesSerializer, \
                            GetSalonServiceSerializer, ApiCitySerializer, EditSalonsSerializer, SelfWhoLoveSerializer, PutMasterFeedbackSerializer, \
                            MasterFeedbackSerializer, GetSalonCatServicesSerializer, GetGlobeCatServicesSerializer, JustSelfMasterSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView, ListAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.template import RequestContext

class IndexView(View):
    def get(self, request):
        return render_to_response('salons/index.html', RequestContext)

class HomeView(ModelViewSet):
    queryset = Salons.objects.all()
    serializer_class = SalonsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ApiFavSalView(ModelViewSet):
    queryset = Salons.objects.all()
    serializer_class = SalonsFavSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ApiListSalonsWorksView(ModelViewSet):
    queryset = Works.objects.all()
    serializer_class = SalonWorksWithLikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ApiListSelfWorksView(ModelViewSet):
    queryset = SelfWorks.objects.all()
    serializer_class = SelfWorksWithLikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ApiSalonPhotosView(ModelViewSet):
    queryset = Photos.objects.all()
    serializer_class = SalonPhotosSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ApiGetSalonServiceView(ModelViewSet):
    queryset = Salons.objects.all()
    serializer_class = GetSalonServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ApiGetSalonWorksView(ModelViewSet):
    queryset = Works.objects.all()
    serializer_class = SalonWorksSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ApiGetSelfWorksView(ModelViewSet):
    queryset = SelfWorks.objects.all()
    serializer_class = SelfWorksSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ApiGetCityView(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = ApiCitySerializer
    permission_classes = [AllowAny]

class ApiSalonFeedbackView(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = SalonFeedbackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ApiMasterFeedbackView(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = MasterFeedbackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ApiSalonBookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = SalonBookSerializer
    permission_classes = [AllowAny]

class ApiBookEditView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookEditSerializer
    permission_classes = [AllowAny]

class ApiSalonCatView(ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = GetSalonCatServicesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ApiGlobeCatView(ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = GetGlobeCatServicesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class AddLikeSalonView(RetrieveUpdateAPIView):
    queryset = Works.objects.all()
    serializer_class = SalonLikeSerializer
    permission_classes = [AllowAny]

class AddLikeSelfMasterView(RetrieveUpdateAPIView):
    queryset = SelfWorks.objects.all()
    serializer_class = SelfWorkLikeSerializer
    permission_classes = [AllowAny]


class PostSalonImage(RetrieveUpdateAPIView):
    queryset = Salons.objects.all()
    serializer_class = PostSalonImageSerializer
    permission_classes = [AllowAny]

class PostSalonFeedback(RetrieveUpdateAPIView):
    queryset = Salons.objects.all()
    serializer_class = PutSalonFeedbackSerializer
    permission_classes = [AllowAny]

class PostSelfFeedback(RetrieveUpdateAPIView):
    queryset = SelfMaster.objects.all()
    serializer_class = PutMasterFeedbackSerializer
    permission_classes = [AllowAny]

class PostSalonBook(RetrieveUpdateAPIView):
    queryset = Salons.objects.all()
    serializer_class = PutSalonBookSerializer
    permission_classes = [AllowAny]

class PostSalonPhoto(RetrieveUpdateAPIView):
    queryset = Salons.objects.all()
    serializer_class = PutSalonPhotosSerializer
    permission_classes = [AllowAny]

class EditPostSalonPhotos(RetrieveUpdateDestroyAPIView):
    queryset = Photos.objects.all()
    serializer_class = SalonPhotosSerializer
    permission_classes = [AllowAny]

class UpView(RetrieveUpdateDestroyAPIView):
    queryset = Salons.objects.all()
    serializer_class = EditSalonsSerializer
    permission_classes = [AllowAny]

class AllSalonsView(ListCreateAPIView):
    queryset = Salons.objects.all()
    serializer_class = AllSalonsSerializer
    permission_classes = [AllowAny]

class AllCreateSalonsView(ListCreateAPIView):
    queryset = Salons.objects.all()
    serializer_class = AllCreateSalonsSerializer
    permission_classes = [AllowAny]


class ListSalonView(ListCreateAPIView):
    serializer_class = AllSalonsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def list(self, request, user):
        queryset = Salons.objects.all().filter(salon_author=user)
        serializer = AllSalonsSerializer(queryset, many=True)
        return Response(serializer.data)
class PostSalonPhotos(ListCreateAPIView):
    queryset = Photos.objects.all()
    serializer_class = SalonPhotosSerializer
    permission_classes = [AllowAny]
class PostSalonFeedbacks(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = SalonFeedbackSerializer
    permission_classes = [AllowAny]
class PostSalonBooks(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = SalonBookSerializer
    permission_classes = [AllowAny]
class MastersSalonView(ListCreateAPIView):
    serializer_class = SalonMastersSerializer
    permission_classes = [AllowAny]
    def list(self, request, pk):
        queryset = Masters.objects.all().filter(salon=pk)
        serializer = SalonMastersSerializer(queryset, many=True)
        return Response(serializer.data)

class ServiceByCatView(ListCreateAPIView):
    serializer_class = GetSalonCatServicesSerializer
    permission_classes = [AllowAny]

    def list(self, request, cat):
        queryset = Services.objects.all().filter(cat=cat)
        serializer = GetSalonCatServicesSerializer(queryset, many=True)
        return Response(serializer.data)


class WorksSalonView(ListCreateAPIView):
    serializer_class = SalonWorksSerializer
    permission_classes = [AllowAny]
    def list(self, request, pk):
        queryset = Works.objects.all().filter(salon=pk)
        serializer = SalonWorksSerializer(queryset, many=True)
        return Response(serializer.data)

class GetSalonServicesView(ListCreateAPIView):
    serializer_class = EditSalonServicesSerializer
    permission_classes = [AllowAny]
    def list(self, request, pk):
        queryset = Salons.objects.all().filter(pk=pk)
        serializer = EditSalonServicesSerializer(queryset, many=True)
        return Response(serializer.data)


class EditMastersSalonView(RetrieveUpdateDestroyAPIView):
    queryset = Masters.objects.all()
    serializer_class = SalonMastersSerializer
    permission_classes = [AllowAny]

class EditWorksSalonView(RetrieveUpdateDestroyAPIView):
    queryset = Works.objects.all()
    serializer_class = SalonWorksSerializer
    permission_classes = [AllowAny]


class ApiServicesView(ModelViewSet):
    queryset = MyService.objects.all()
    serializer_class = SalonServicesSerializer
    permission_classes = [AllowAny]

class MyServiceByService(ListAPIView):
    serializer_class = SalonServicesSerializer
    permission_classes = [AllowAny]

    def list(self, request, service):
        queryset = MyService.objects.all().filter(service=service)
        serializer = SalonServicesSerializer(queryset, many=True)
        return Response(serializer.data)




class ServicesView(ListCreateAPIView):
    queryset = MyService.objects.all()
    serializer_class = SalonServicesSerializer
    permission_classes = [AllowAny]

class EditServicesView(RetrieveUpdateDestroyAPIView):
    queryset = MyService.objects.all()
    serializer_class = SalonServicesSerializer
    permission_classes = [AllowAny]

class EditSalonServices(RetrieveUpdateDestroyAPIView):
    queryset = Salons.objects.all()
    serializer_class = EditSalonServicesSerializer
    permission_classes = [AllowAny]


class EditValueOfSalonView(RetrieveUpdateDestroyAPIView):
    queryset = ValueOfSalon.objects.all()
    serializer_class = ValueOfSalonSerializer
    permission_classes = [AllowAny]

class CatServicesSalonView(ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = SalonCatServicesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ApiProfleView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
class ApiUserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
class ApiMastersView(ModelViewSet):
    queryset = SelfMaster.objects.all()
    serializer_class = SelfMasterSerializer
    permission_classes = [AllowAny]




class UserGetPkView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def list(self, request, username):
        queryset = User.objects.all().filter(username=username)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)



class ValueOfSalonView(ListAPIView):
    serializer_class = ValueOfSalonSerializer
    permission_classes = [AllowAny]

    def list(self, request, salon):
        queryset = ValueOfSalon.objects.all().filter(salon=salon)
        serializer = ValueOfSalonSerializer(queryset, many=True)
        return Response(serializer.data)



class ApiWhoLoveMasterView(ModelViewSet):
    queryset = SelfMaster.objects.all()
    serializer_class = SelfWhoLoveSerializer
    permission_classes = [AllowAny]





class ApiUserLogoView(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserLogoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EditUserLogoView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserLogoSerializer
    permission_classes = [AllowAny]
class ListUserLogoView(ListCreateAPIView):
    serializer_class = UserLogoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def list(self, request, user):
        queryset = UserProfile.objects.all().filter(user=user)
        serializer = UserLogoSerializer(queryset, many=True)
        return Response(serializer.data)
class EditUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = EditUserSerializer
    permission_classes = [AllowAny]
class EditProfileView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]
class ApiValueOfSalonView(ModelViewSet):
    queryset = ValueOfSalon.objects.all()
    serializer_class = ValueOfSalonSerializer
    permission_classes = [AllowAny]
class PostProfileView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = PostUserProfileSerializer
    permission_classes = [AllowAny]
class ListProfileView(ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def list(self, request, user):
        queryset = UserProfile.objects.all().filter(user=user)
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)








class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

class LoginUserView(APIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginUserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data=serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ExLoginUserView(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class DetailView(generic.DetailView):
    model = Salons
    template_name = 'salons/detail.html'

    def get_context_data(self, *args, **kwargs):
        args = super(DetailView, self).get_context_data(**kwargs)
        salon = Salons.objects.get(pk=self.kwargs['pk'])
        user = auth.get_user(self.request)
        notuser = User.objects.get(pk=salon.salon_author.pk)
        if user != notuser:
            # return HttpResponseRedirect('/salons')
            args['itsme'] = False
        else:
            args['itsme'] = True
            args['user'] = user
        return args






# Create your views here.
#class HomeView(generic.ListView):
#    def get(self, request):
#        args = {}
#        args['all_salons'] = Salons.objects.all().order_by('-pk')[:5]
#        args['user'] = auth.get_user(request)
#        return render_to_response('salons/home.html', args)



class ProfileView(generic.DetailView):
    model = User
    template_name = 'salons/profile.html'

    def get(self, request, pk):
        args = {}
        args['salons'] = Salons.objects.filter(salon_author=pk)
        args['user'] = User.objects.get(pk=pk)
        user = auth.get_user(request)
        notuser = User.objects.get(pk=pk)
        if user != notuser:
            #return HttpResponseRedirect('/salons')
            args['itsme'] = False
        else:
            args['itsme'] = True
        return render_to_response(self.template_name, args)





class UserFormView(View):
    form_class = UserForm
    template_name = 'salons/registrations_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/salons')
        return render(request, self.template_name, {'form': form})


decorators = [never_cache, csrf_protect]

@method_decorator(decorators, name='post')
class LoginView(View):
    form_class = LoginForm
    template_name = 'salons/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        method_decorator(csrf_protect)
        form = self.form_class(request.POST)
        c = {}
        c['form'] = self.form_class(None)

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('salons:home')
        else:
            c['login_error'] = "User is not exist"
            return render(request, self.template_name, c)
        return render(request, self.template_name, c)

class LogoutView(View):
    def get(self, request):
       logout(request)
       return redirect('salons:home')



decorators = [never_cache, csrf_protect]

@method_decorator(decorators, name='post')
class AddMySalonsView(View):
    model = SalonsForm

    def get(self, request, pk):
        form = SalonsForm
        args = {}
        args['user'] = User.objects.get(pk=pk)
        args['form'] = form
        return render_to_response('salons/addsalon.html', args)

    def post(self, request, pk):
        method_decorator(csrf_protect)
        args = {}
        args['salons'] = Salons.objects.filter(salon_author=pk)
        args['user'] = User.objects.get(pk=pk)
        form = SalonsForm(request.POST or None, request.FILES or None)
        if request.POST:
            user = User.objects.get(pk=pk)
            if form.is_valid():
                salon = form.save(commit=False)
                salon.salon_author = user
                salon.save()
            return render_to_response('salons/profile.html', args)

class SalonUpdate(UpdateView):
    model = Salons
    fields = ['name', 'salon_desc', 'salon_adress', 'salon_logo']
    template_name = 'salons_form.html'

class SalonDelete(DeleteView):
    model = Salons
    success_url = reverse_lazy('salons:home')













class ApiSelfMasterView(ModelViewSet):
    queryset = SelfMaster.objects.all()
    serializer_class = SelfMasterSerializer
    permission_classes = [AllowAny]


class ApiJustSelfMasterView(ModelViewSet):
    queryset = SelfMaster.objects.all()
    serializer_class = JustSelfMasterSerializer
    permission_classes = [AllowAny]


class ApiSelfServicesMasterView(ModelViewSet):
    queryset = SelfMaster.objects.all()
    serializer_class = SelfMasterServicesSerializer
    permission_classes = [AllowAny]





class ListSelfMasterView(ListAPIView):
    serializer_class = SelfMasterSerializer
    permission_classes = [AllowAny]
    def list(self, request, user):
        queryset = SelfMaster.objects.all().filter(master_author=user)
        serializer = SelfMasterSerializer(queryset, many=True)
        return Response(serializer.data)



class ListSelfServicesMasterView(ListAPIView):
    serializer_class = SelfMasterServicesSerializer
    permission_classes = [AllowAny]
    def list(self, request, user):
        queryset = SelfMaster.objects.all().filter(master_author=user)
        serializer = SelfMasterServicesSerializer(queryset, many=True)
        return Response(serializer.data)

class CreateSelfWorkView(ListCreateAPIView):
    queryset = SelfWorks.objects.all()
    serializer_class = SelfWorksSerializer
    permission_classes = [AllowAny]

    def list(self, request, master):
        queryset = SelfWorks.objects.all().filter(master=master)
        serializer = SelfWorksSerializer(queryset, many=True)
        return Response(serializer.data)

class SelfValueOfMasterView(ListCreateAPIView):
    serializer_class = SelfValueOfMasterSerializer
    permission_classes = [AllowAny]

    def list(self, request, master):
        queryset = SelfValueOfMaster.objects.all().filter(master=master)
        serializer = SelfValueOfMasterSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateValueOfSalonView(ListCreateAPIView):
    queryset = SelfValueOfMaster.objects.all()
    serializer_class = SelfValueOfMasterSerializer
    permission_classes = [AllowAny]

class CreateValueOfSelfView(ListCreateAPIView):
    queryset = ValueOfSalon.objects.all()
    serializer_class = ValueOfSalonSerializer
    permission_classes = [AllowAny]


class EditSelfMasterView(RetrieveUpdateDestroyAPIView):
    queryset = SelfMaster.objects.all()
    serializer_class = JustSelfMasterSerializer
    permission_classes = [AllowAny]

class EditSelfServicesView(RetrieveUpdateDestroyAPIView):
    queryset = SelfMaster.objects.all()
    serializer_class = SelfServiceSerializer
    permission_classes = [AllowAny]

class EditSelfWorkView(RetrieveUpdateDestroyAPIView):
    queryset = SelfWorks.objects.all()
    serializer_class = SelfWorksSerializer
    permission_classes = [AllowAny]

class EditSelfValueOfMasterView(RetrieveUpdateDestroyAPIView):
    queryset = SelfValueOfMaster.objects.all()
    serializer_class = SelfValueOfMasterSerializer
    permission_classes = [AllowAny]

class EditLikeWorkView(RetrieveUpdateDestroyAPIView):
    queryset = SelfWorks.objects.all()
    serializer_class = SelfLikeSerializer
    permission_classes = [AllowAny]



class WhoLoveMasterView(RetrieveUpdateDestroyAPIView):
    queryset = SelfMaster.objects.all()
    serializer_class = SelfWhoLoveSerializer
    permission_classes = [AllowAny]



class ListFavMastersView(ListCreateAPIView):
    queryset = FavMasters.objects.all()
    serializer_class = FavMastersSerializer
    permission_classes = [AllowAny]

class ListFavSalonsView(ListCreateAPIView):
    queryset = FavSalons.objects.all()
    serializer_class = FavSalonsSerializer
    permission_classes = [AllowAny]

class CreateFavMastersView(ListCreateAPIView):
    serializer_class = FavMastersSerializer
    permission_classes = [AllowAny]

    def list(self, request, user):
        queryset = FavMasters.objects.all().filter(user=user)
        serializer = FavMastersSerializer(queryset, many=True)
        return Response(serializer.data)

class CreateFavSalonsView(ListCreateAPIView):
    serializer_class = FavSalonsSerializer
    permission_classes = [AllowAny]

    def list(self, request, user):
        queryset = FavSalons.objects.all().filter(user=user)
        serializer = FavSalonsSerializer(queryset, many=True)
        return Response(serializer.data)


class ByMasterFavMastersView(ListAPIView):
    serializer_class = FavMastersSerializer
    permission_classes = [AllowAny]

    def list(self, request, master):
        queryset = FavMasters.objects.all().filter(master=master)
        serializer = FavMastersSerializer(queryset, many=True)
        return Response(serializer.data)

class BySalonFavSalonsView(ListAPIView):
    serializer_class = FavSalonsSerializer
    permission_classes = [AllowAny]

    def list(self, request, salon):
        queryset = FavSalons.objects.all().filter(salon=salon)
        serializer = FavSalonsSerializer(queryset, many=True)
        return Response(serializer.data)


class EditFavSalonsView(RetrieveUpdateDestroyAPIView):
    queryset = FavSalons.objects.all()
    serializer_class = FavSalonsSerializer
    permission_classes = [AllowAny]

class EditFavMastersView(RetrieveUpdateDestroyAPIView):
    queryset = FavMasters.objects.all()
    serializer_class = FavMastersSerializer
    permission_classes = [AllowAny]
























