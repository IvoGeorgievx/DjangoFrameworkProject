from rest_framework import generics as rest_views, views, exceptions, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from project_watches.api.serializers import ProfileDetailsSerializer, WatchesSerializer, WalletSerializer, \
    SunglassesSerializer, BeltsSerializer, TiesSerializer
from project_watches.auth_app.models import Profile
from project_watches.web.models import Watches, Wallets, Sunglasses, Belts, Ties
from rest_framework import permissions


class CustomAdminPermission(permissions.BasePermission):
    message = 'You do not have permissions to view that.'

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class ProfileDetailsApiView(rest_views.ListCreateAPIView):
    AGE = 18
    queryset = Profile.objects.all()
    serializer_class = ProfileDetailsSerializer
    permission_classes = [CustomAdminPermission]

    def get_queryset(self):
        queryset = Profile.objects.all()
        # filtering Profiles with age >= 18 and not null first name and last name
        queryset = queryset.filter(age__gte=self.AGE,
                                   first_name__isnull=False,
                                   last_name__isnull=False)
        return queryset


class WatchesApiView(rest_views.ListAPIView):
    queryset = Watches.objects.all()
    serializer_class = WatchesSerializer
    permission_classes = [IsAuthenticated]


class CreateWatchApiView(rest_views.CreateAPIView):
    serializer_class = WatchesSerializer
    permission_classes = [IsAdminUser]


class WalletsApiView(rest_views.ListAPIView):
    queryset = Wallets.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]


class SunglassesApiView(rest_views.ListAPIView):
    queryset = Sunglasses.objects.all()
    serializer_class = SunglassesSerializer
    permission_classes = [IsAuthenticated]


class BeltsApiView(rest_views.ListAPIView):
    queryset = Belts.objects.all()
    serializer_class = BeltsSerializer
    permission_classes = [IsAuthenticated]


class TiesApiView(rest_views.ListAPIView):
    queryset = Ties.objects.all()
    serializer_class = TiesSerializer
    permission_classes = [IsAuthenticated]
