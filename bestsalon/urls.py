
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'allsalons'

router = routers.SimpleRouter()
router.register(r'sal', views.HomeView)
router.register(r'salFav', views.ApiFavSalView)
router.register(r'users', views.ApiUserView)
router.register(r'profile', views.ApiProfleView)
router.register(r'userlogo', views.ApiUserLogoView)
router.register(r'addvalueofsalon', views.ApiValueOfSalonView)
router.register(r'masters', views.ApiMastersView)
router.register(r'listsalonworks', views.ApiListSalonsWorksView)
router.register(r'listselfworks', views.ApiListSelfWorksView)
router.register(r'salonphotos', views.ApiSalonPhotosView)
router.register(r'salonfeedback', views.ApiSalonFeedbackView)
router.register(r'masterfeedback', views.ApiMasterFeedbackView)
router.register(r'salonbook', views.ApiSalonBookView)
router.register(r'bookedit', views.ApiBookEditView)
router.register(r'saloncat', views.ApiSalonCatView)
router.register(r'globecat', views.ApiGlobeCatView)
router.register(r'selfmaster', views.ApiSelfMasterView)
router.register(r'justselfmaster', views.ApiJustSelfMasterView)
router.register(r'services', views.ApiServicesView)
router.register(r'selfmasterservices', views.ApiSelfServicesMasterView)
router.register(r'salonservices', views.ApiGetSalonServiceView)
router.register(r'wholovemaster', views.ApiWhoLoveMasterView)
router.register(r'getsalonworks', views.ApiGetSalonWorksView)
router.register(r'getselfworks', views.ApiGetSelfWorksView)
router.register(r'getcity', views.ApiGetCityView)






urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^sal$', views.IndexView.as_view(), name='index'),
    url(r'^sal/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^api/edit/(?P<pk>[0-9]+)/$', views.UpView.as_view(), name="upview"),
    url(r'^api/all/$', views.AllSalonsView.as_view(), name="allsalonsview"),
    url(r'^api/allcreate/$', views.AllCreateSalonsView.as_view(), name="allcreate"),
    url(r'^api/editimg/(?P<pk>[0-9]+)/$', views.PostSalonImage.as_view(), name="upimgview"),
    url(r'^api/editPhoto/(?P<pk>[0-9]+)/$', views.PostSalonPhoto.as_view(), name="editPhoto"),
    url(r'^api/editPhotos/(?P<pk>[0-9]+)/$', views.EditPostSalonPhotos.as_view(), name="editPhotos"),
    url(r'^api/editFeedback/(?P<pk>[0-9]+)/$', views.PostSalonFeedback.as_view(), name="editFeedback"),
    url(r'^api/editSelfFeedback/(?P<pk>[0-9]+)/$', views.PostSelfFeedback.as_view(), name="editFeedback"),
    url(r'^api/editBook/(?P<pk>[0-9]+)/$', views.PostSalonBook.as_view(), name="editBook"),
    url(r'^api/postphotos/$', views.PostSalonPhotos.as_view(), name="postphotos"),
    url(r'^api/postfeedback/$', views.PostSalonFeedbacks.as_view(), name="postfeedback"),
    url(r'^api/postbook/$', views.PostSalonBooks.as_view(), name="postbook"),

    url(r'^api/servicebycat/(?P<cat>\w+)/$', views.ServiceByCatView.as_view(), name="servicebycat"),

    url(r'^api/mylist/(?P<user>\w+)/$', views.ListSalonView.as_view(), name="mylist"),

    url(r'^api/myservice/(?P<service>[0-9]+)/$', views.MyServiceByService.as_view(), name="myservice"),

    url(r'^api/salonmasters/(?P<pk>[0-9]+)/$', views.MastersSalonView.as_view(), name="masterview"),
    url(r'^api/salonworks/(?P<pk>[0-9]+)/$', views.WorksSalonView.as_view(), name="workview"),
    url(r'^api/salonservices/$', views.ServicesView.as_view(), name="serviceview"),
    url(r'^api/salonscatservices/$', views.CatServicesSalonView.as_view(), name="catserviceview"),
    url(r'^api/salonsvalues/(?P<salon>[0-9]+)/$', views.ValueOfSalonView.as_view(), name="salonsvalues"),
    url(r'^api/salonslike/(?P<pk>[0-9]+)/$', views.AddLikeSalonView.as_view(), name="salonslike"),
    url(r'^api/getsalonservice/(?P<pk>[0-9]+)/$', views.GetSalonServicesView.as_view(), name="getsalonservice"),

    url(r'^api/salonsvalues/$', views.CreateValueOfSalonView.as_view(), name="salonsvalues"),
    url(r'^api/selfvalues/$', views.CreateValueOfSelfView.as_view(), name="selfvalues"),

    url(r'^api/salonmasters/edit/(?P<pk>[0-9]+)/$', views.EditMastersSalonView.as_view(), name="editmasterview"),
    url(r'^api/salonworks/edit/(?P<pk>[0-9]+)/$', views.EditWorksSalonView.as_view(), name="editworkview"),
    url(r'^api/editsalonservices/edit/(?P<pk>[0-9]+)/$', views.EditSalonServices.as_view(), name="editsalonservices"),
    url(r'^api/salonservices/edit/(?P<pk>[0-9]+)/$', views.EditServicesView.as_view(), name="editserviceview"),
    url(r'^api/salonsvalues/edit/(?P<pk>[0-9]+)/$', views.EditValueOfSalonView.as_view(), name="editsalonsvalues"),

    url(r'^api/getselfmaster/(?P<user>[0-9]+)/$', views.ListSelfMasterView.as_view(), name="getselfmaster"),
    url(r'^api/selfservices/(?P<user>[0-9]+)/$', views.ListSelfServicesMasterView.as_view(), name="selfservices"),
    url(r'^api/selfworks/(?P<master>[0-9]+)/$', views.CreateSelfWorkView.as_view(), name="selfworks"),
    url(r'^api/selfvalues/(?P<master>[0-9]+)/$', views.SelfValueOfMasterView.as_view(), name="selfvalues"),
    url(r'^api/selflike/(?P<pk>[0-9]+)/$', views.AddLikeSelfMasterView.as_view(), name="selflike"),



    url(r'^api/wholovemaster/edit/(?P<pk>[0-9]+)/$', views.WhoLoveMasterView.as_view(), name="wholovemaster"),
    url(r'^api/selfmaster/edit/(?P<pk>[0-9]+)/$', views.EditSelfMasterView.as_view(), name="editselfmaster"),
    url(r'^api/selfservices/edit/(?P<pk>[0-9]+)/$', views.EditSelfServicesView.as_view(), name="editselfservices"),
    url(r'^api/selfworks/edit/(?P<pk>[0-9]+)/$', views.EditSelfWorkView.as_view(), name="editselfworks"),
    url(r'^api/selfvalues/edit/(?P<pk>[0-9]+)/$', views.EditSelfValueOfMasterView.as_view(), name="editselfvalues"),
    url(r'^api/selfworklike/edit/(?P<pk>[0-9]+)/$', views.EditLikeWorkView.as_view(), name="editselfworklike"),



    url(r'^api/favsalon/$', views.ListFavSalonsView.as_view(), name="listfavsalon"),
    url(r'^api/favmaster/$', views.ListFavMastersView.as_view(), name="listfavmaster"),

    url(r'^api/bymaster/(?P<master>[0-9]+)/$', views.ByMasterFavMastersView.as_view(), name="bymaster"),
    url(r'^api/bysalon/(?P<salon>[0-9]+)/$', views.BySalonFavSalonsView.as_view(), name="bysalon"),
    url(r'^api/favsalon/(?P<user>[0-9]+)/$', views.CreateFavSalonsView.as_view(), name="createfavsalon"),
    url(r'^api/favmaster/(?P<user>[0-9]+)/$', views.CreateFavMastersView.as_view(), name="createfavmaster"),
    url(r'^api/favsalon/edit/(?P<pk>[0-9]+)/$', views.EditFavSalonsView.as_view(), name="editfavsalon"),
    url(r'^api/favmaster/edit/(?P<pk>[0-9]+)/$', views.EditFavMastersView.as_view(), name="editfavmaster"),



    url(r'^api/usergetpk/(?P<username>\w+)/$', views.UserGetPkView.as_view(), name="usergetpk"),

    url(r'^api/userlogo/edit/(?P<pk>[0-9]+)/$', views.EditUserLogoView.as_view(), name="edituserlogoview"),
    url(r'^api/userlogo/list/(?P<user>[0-9]+)/$', views.ListUserLogoView.as_view(), name="listuserlogoview"),
    url(r'^api/user/edit/(?P<pk>[0-9]+)/$', views.EditUserView.as_view(), name="edituserview"),

    url(r'^api/postprofile/post/$', views.PostProfileView.as_view(), name="postprofileview"),
    url(r'^api/listprofile/list/(?P<user>[0-9]+)/$', views.ListProfileView.as_view(), name="editprofileview"),
    url(r'^api/profile/edit/(?P<pk>[0-9]+)/$', views.EditProfileView.as_view(), name="editprofileview"),

    url(r'^api/register/$', views.CreateUserView.as_view(), name="createuserview"),
    url(r'^api/login/$', views.LoginUserView.as_view(), name="loginuserview"),
    url(r'^api/exlogin/$', views.ExLoginUserView.as_view(), name="exloginuserview"),

    url(r'^api-token-auth/', obtain_jwt_token),


    #url(r'^api/users/$', views.ApiUserView.as_view(), name="apiuserview"),
    #url(r'^api/profile/$', views.ApiProfleView.as_view(), name="apiprofileview"),


    #    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    url(r'^profile/(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name="profile"),
    url(r'^profile/(?P<pk>[0-9]+)/addmysalons/$', views.AddMySalonsView.as_view(), name="addmysalons"),
    url(r'^(?P<pk>[0-9]+)/update/$', views.SalonUpdate.as_view(), name='salon-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.SalonDelete.as_view(), name='salon-delete'),
]
