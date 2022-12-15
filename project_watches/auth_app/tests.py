from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from project_watches.auth_app.forms import EditProfileForm, SignUpForm, DeleteProfileForm
from project_watches.auth_app.models import Profile


class ProfileModelTests(TestCase):

    def test_profile_save__when_name_is_alphabet__expect_success(self):
        user = User.objects.create(username='Something', password='Asdasd123')
        profile = Profile(
            first_name='Ivo',
            last_name='Georgiev',
            user=user
        )
        user.full_clean()
        user.save()
        profile.full_clean()
        profile.save()

        self.assertIsNotNone(user.pk)
        self.assertIsNotNone(profile.pk)

    def test_profile_save__when_name_is_incorrect__expect_exception(self):
        user = User.objects.create(username='Something', password='Asdasd123')
        profile = Profile(
            first_name='Ivo1',
            last_name='Georgiev',
            user=user
        )

        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_user_logged__when_registered__expect_logged_in(self):
        user = User.objects.create(username='Something', password='Asdasd123')

        self.assertTrue(user.is_authenticated)
        self.assertFalse(user.is_anonymous)


class AuthFormsTests(TestCase):
    def test_edit_profile__when_form_is_valid__expect_edited(self):
        data = {
            'first_name': 'Ivo',
            'last_name': 'Georgiev',
            'email': 'testmail@abv.bg',
            'gender': 'Male',
            'age': 25,

        }

        form = EditProfileForm(data)

        self.assertTrue(form.is_valid())

    def test_edit_profile__when_form_is_not_valid__expect_False(self):
        data = {
            'first_name': 'Ivo12',
            'last_name': 'Georgiev!!',
            'email': 'testmail@abv.bg',
            'gender': 'Male',
            'age': 25,

        }

        form = EditProfileForm(data)

        self.assertFalse(form.is_valid())
