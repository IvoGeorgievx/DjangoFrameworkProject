from django.urls import path

from project_watches.auth_app.views import SignUpView, UserListView, SignInView, SignOutView, ProfileDetailsView, \
    DeleteProfileView, EditProfileView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('users/', UserListView.as_view(), name='user list'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
    path('user/details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('user/edit/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('user/delete/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),

)
