from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views, get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms, authenticate, login
from project_watches.auth_app.forms import SignUpForm, EditProfileForm, DeleteProfileForm, ContactForm
from project_watches.auth_app.models import Profile

UserModel = get_user_model()


def custom_404_error(request, exception):
    return render(request, 'errors/404.html')


class SignUpView(views.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return self.get_redirect_url() or self.get_default_redirect_url()


class UserListView(PermissionRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'auth/users.html'
    permission_required = ('is_superuser',)


class SignOutView(auth_views.LogoutView):
    template_name = 'auth/sign-out.html'


class ProfileDetailsView(views.DetailView):
    template_name = 'auth/user-details.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.object.pk
        return context


class EditProfileView(LoginRequiredMixin, views.UpdateView):
    template_name = 'auth/edit-profile.html'
    form_class = EditProfileForm
    model = Profile
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return Profile.objects.filter(pk=self.request.user.pk).get()


class DeleteProfileView(LoginRequiredMixin, views.DeleteView):
    template_name = 'auth/delete-profile.html'
    form_class = DeleteProfileForm
    model = Profile
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        success_url = self.get_success_url()
        User.objects.filter(pk=self.object.pk).get().delete()
        self.object.delete()
        return HttpResponseRedirect(success_url)

    def get_queryset(self):
        return Profile.objects.all()
