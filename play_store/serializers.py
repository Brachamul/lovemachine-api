from .models import App
from rest_framework import serializers


class AppSerializer(serializers.HyperlinkedModelSerializer):

    def run_validators(self, value):
        for validator in self.validators:
            if isinstance(validator, validators.UniqueTogetherValidator):
                self.validators.remove(validator)
        super(AppSerializer, self).run_validators(value)

    def create(self, validated_data):
        instance, _ = App.objects.update_or_create(store_id=validated_data['store_id'], defaults=validated_data)
        return instance

    class Meta:
        model = App
        fields = [
            'url', 'store_id', 'name', 'dev_id', 'category', 'subcategory',
            'short_description', 'long_description', 'thumbnail',
            'screenshots', 'rating', 'reviews', 'installs', 'maturity',
            'size', 'is_free', 'display_price', 'full_price', 'has_ads',
            'has_iaps', 'current_version', 'android_version', 'last_updated',
        ]
        extra_kwargs = {
            'url': {'lookup_field': 'store_id'},
            'store_id': {'validators': []},
        }


'''

    def create(self, validated_data):
        app = App.objects.get(store_id=validated_data['store_id'])
        app.update(**validated_data)
        app.save()
        return instance


'''