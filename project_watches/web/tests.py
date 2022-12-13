from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from project_watches.web.forms import EditWatchForm
from project_watches.web.models import Watches, Belts


class ValidatorsTests(TestCase):

    def test_create_watch_validator_with_valid_years__expect_register(self):
        watch = Watches(
            name='Test',
            year='2011',
            description='Something',
            price=100,

        )

        watch.full_clean()
        watch.save()

        self.assertIsNotNone(watch.pk)

    def test_create_watch_validator__with_invalid_years__expect_error(self):
        watch = Watches(
            name='Test',
            year='2031',
            description='Something',
            price=100,

        )

        with self.assertRaises(ValidationError) as context:
            watch.full_clean()
            watch.save()

        self.assertIsNotNone(context.exception)

    def test_create_belt__with_valid_price__expect_creation(self):
        belt = Belts(
            brand='SomeBrand',
            color='Black',
            material='Leather',
            buckle_form='Default',
            price=110,
        )

        belt.full_clean()
        belt.save()

        self.assertIsNotNone(belt.pk)

    def test_create_belt__with_invalid_price_expect_exception(self):
        belt = Belts(
            brand='SomeBrand',
            color='Black',
            material='Leather',
            buckle_form='Default',
            price=255,
        )
        with self.assertRaises(ValidationError) as context:
            belt.full_clean()
            belt.save()
        self.assertIsNotNone(context.exception)


class WebFormsTests(TestCase):
    def test_watch_form__edited_correctly__expect_true(self):
        data = {
            'name': 'TestName',
            'year': 2001,
            'description': 'some text',
            'price': 215,

        }
        form = EditWatchForm(data)

        self.assertTrue(form.is_valid())

    def test_watch_form__edited_incorrectly__expect_exception(self):
        data = {
            'name': 'TestName',
            'year': 2044,
            'description': 'some text',
            'price': 215,

        }
        form = EditWatchForm(data)

        self.assertFalse(form.is_valid())


class WebViewsTests(TestCase):

    def test_user_details__when_owner__expect_is_owner_true(self):
        pass
