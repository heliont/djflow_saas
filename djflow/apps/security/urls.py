from django.urls import path
from .views import Login, Logout
from .views import UserProfileData, UserList, UserNew, UserDelete
from .views import ActiveInactiveUser, ChangePassword
from .views import TenantRegisterView

app_name = 'security'

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('userprofile/', UserProfileData.as_view(), name="userprofile"),
    path('userprofilechange-password/', ChangePassword.as_view(), name="userprofile-change-password"),
    path('user/list/', UserList.as_view(), name="user-list"),
    path('user/new/', UserNew.as_view(), name="user-new"),
    path('user/delete/(?P<pk>.*)/', UserDelete.as_view(), name="user-delete"),
    path('user/active-inactive/(?P<user_id>.*)/', ActiveInactiveUser.as_view(), name="user-active-inactive"),
    path('tenant/register/', TenantRegisterView.as_view(), name="tenant-register"),
]



