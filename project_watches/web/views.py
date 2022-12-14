from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from project_watches.auth_app.forms import ContactForm
from project_watches.web.forms import EditWatchForm, EditWalletForm, EditSunglassesForm, EditBeltsForm, EditTiesForm
from project_watches.web.models import Watches, Wallets, Sunglasses, Belts, Ties


def custom_404_error(request, exception):
    return render(request, 'errors/404.html')


def custom_500_error(request):
    return render(request, 'errors/500.html')


def index(request):
    return render(request, 'base.html')


def about_view(request):
    return render(request, 'web/about.html')


class ContactsView(views.CreateView):
    template_name = 'web/contacts.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')


class WatchesView(views.ListView):
    template_name = 'web/watches.html'
    model = Watches
    paginate_by = 1


class WatchDetailsView(views.DetailView):
    template_name = 'web/watch-details.html'
    model = Watches


class EditWatchView(PermissionRequiredMixin, views.UpdateView):
    template_name = 'web/edit-watch.html'
    form_class = EditWatchForm
    model = Watches
    success_url = reverse_lazy('watches view')
    permission_required = ('web.view_watches', 'web.change_watches',)


class WalletsView(views.ListView):
    template_name = 'web/wallets.html'
    model = Wallets
    paginate_by = 1


class WalletDetailsView(views.DetailView):
    template_name = 'web/wallet-details.html'
    model = Wallets


class EditWalletView(PermissionRequiredMixin, views.UpdateView):
    template_name = 'web/edit-wallet.html'
    form_class = EditWalletForm
    model = Wallets
    success_url = reverse_lazy('wallets view')
    permission_required = ('web.view_wallets', 'web.change_wallets',)


class SunglassesView(views.ListView):
    template_name = 'web/sunglasses.html'
    model = Sunglasses
    paginate_by = 1


class SunglassesDetailsView(views.DetailView):
    template_name = 'web/sunglasses-details.html'
    model = Sunglasses


class EditSunglassesView(PermissionRequiredMixin, views.UpdateView):
    template_name = 'web/edit-sunglasses.html'
    form_class = EditSunglassesForm
    model = Sunglasses
    success_url = reverse_lazy('sunglasses view')
    permission_required = ('web.view_sunglasses', 'web.change_sunglasses',)


class BeltsView(views.ListView):
    template_name = 'web/belts.html'
    model = Belts
    paginate_by = 1


class BeltsDetailsView(views.DetailView):
    template_name = 'web/belts-details.html'
    model = Belts


class EditBeltsView(PermissionRequiredMixin, views.UpdateView):
    template_name = 'web/edit-belts.html'
    form_class = EditBeltsForm
    model = Belts
    success_url = reverse_lazy('belts view')
    permission_required = ('web.view_belts', 'web.change_belts',)


class TiesView(views.ListView):
    template_name = 'web/ties.html'
    model = Ties
    paginate_by = 1


class TiesDetailsView(views.DetailView):
    template_name = 'web/tie-details.html'
    model = Ties


class EditTiesView(PermissionRequiredMixin, views.UpdateView):
    template_name = 'web/edit-ties.html'
    form_class = EditTiesForm
    model = Ties
    success_url = reverse_lazy('ties view')
    permission_required = ('web.view_ties', 'web.change_belts',)
