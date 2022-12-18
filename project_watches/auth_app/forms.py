from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import forms as auth_forms
from project_watches.auth_app.models import Profile, Contact


class SignUpForm(auth_forms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'

    class Meta:
        model = User
        fields = ("username",)

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            user=user,
        )
        if commit:
            profile.save()
        return user


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user', 'username')


class EditProfileForm(BaseProfileForm):
    pass


class DeleteProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = ()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description here.'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your name here.'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter your email here.'
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the subject here.'
                }
            ),
        }
