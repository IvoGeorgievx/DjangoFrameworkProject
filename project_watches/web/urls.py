from django.urls import path
from project_watches.web.views import index, WatchesView, WatchDetailsView, WalletsView, \
    WalletDetailsView, SunglassesView, SunglassesDetailsView, EditWatchView, EditWalletView, EditSunglassesView, \
    BeltsView, BeltsDetailsView, EditBeltsView, TiesView, TiesDetailsView, EditTiesView, ContactsView, about_view

urlpatterns = (
    path('', index, name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts view'),
    path('about/', about_view, name='about view'),
    path('gallery/watches/', WatchesView.as_view(), name='watches view'),
    path('gallery/watches/<int:pk>/', WatchDetailsView.as_view(), name='watch details'),
    path('gallery/wallets/', WalletsView.as_view(), name='wallets view'),
    path('gallery/wallets/<int:pk>/', WalletDetailsView.as_view(), name='wallet details'),
    path('gallery/sunglasses/', SunglassesView.as_view(), name='sunglasses view'),
    path('gallery/sunglasses/<int:pk>/', SunglassesDetailsView.as_view(), name='sunglasses details'),
    path('watches/edit/<int:pk>/', EditWatchView.as_view(), name='edit watch'),
    path('wallets/edit/<int:pk>/', EditWalletView.as_view(), name='edit wallet'),
    path('sunglasses/edit/<int:pk>/', EditSunglassesView.as_view(), name='edit sunglasses'),
    path('gallery/belts/', BeltsView.as_view(), name='belts view'),
    path('gallery/belts/<int:pk>/', BeltsDetailsView.as_view(), name='belts details'),
    path('belts/edit/<int:pk>/', EditBeltsView.as_view(), name='edit belts'),
    path('gallery/ties/', TiesView.as_view(), name='ties view'),
    path('gallery/ties/<int:pk>/', TiesDetailsView.as_view(), name='ties details'),
    path('belts/edit/<int:pk>', EditTiesView.as_view(), name='edit ties'),

)
