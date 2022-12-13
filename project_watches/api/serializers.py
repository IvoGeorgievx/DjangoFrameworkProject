from rest_framework import serializers
from project_watches.auth_app.models import Profile
from project_watches.web.models import Watches, Wallets, Sunglasses, Belts, Ties


class ProfileDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('pk', 'first_name', 'last_name', 'age')


class WatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watches
        fields = '__all__'


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallets
        fields = '__all__'


class SunglassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sunglasses
        fields = '__all__'


class BeltsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Belts
        fields = '__all__'


class TiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ties
        fields = '__all__'
