from django.urls import path

from project_watches.api.views import ProfileDetailsApiView, WatchesApiView, WalletsApiView, SunglassesApiView, \
    BeltsApiView, TiesApiView, CreateWatchApiView

urlpatterns = (
    path('details/', ProfileDetailsApiView.as_view(), name='api details view'),
    path('watches/', WatchesApiView.as_view(), name='api watches view'),
    path('watches/create/', CreateWatchApiView.as_view(), name='api create watch view'),
    path('wallets/', WalletsApiView.as_view(), name='api wallets view'),
    path('sunglasses/', SunglassesApiView.as_view(), name='api sunglasses view'),
    path('belts/', BeltsApiView.as_view(), name='api sunglasses view'),
    path('ties/', TiesApiView.as_view(), name='api sunglasses view'),
)
