from django import forms

from project_watches.web.models import Watches, Wallets, Sunglasses, Belts, Ties


class EditWatchForm(forms.ModelForm):
    class Meta:
        model = Watches
        fields = '__all__'


class EditWalletForm(forms.ModelForm):
    class Meta:
        model = Wallets
        fields = '__all__'


class EditSunglassesForm(forms.ModelForm):
    class Meta:
        model = Sunglasses
        fields = '__all__'


class EditBeltsForm(forms.ModelForm):
    class Meta:
        model = Belts
        fields = '__all__'


class EditTiesForm(forms.ModelForm):
    class Meta:
        model = Ties
        fields = '__all__'
