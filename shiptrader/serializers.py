from rest_framework import serializers

from .models import Starship


class StarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starship
        fields = [
            'name',
            'model',
            'starship_class',
            'manufacturer',
            'length',
            'hyperdrive_rating',
            'cargo_capacity',
            'crew',
            'passengers',
        ]

    def to_internal_value(self, data):
        """
        Handle esoteric SWAPI values if necessary, for object creation.
        :param data: Dict of unvalidated input.
        :return: Modified validated_data dict.
        """
        for field, value in data.items():
            if str(value).lower() in ('unknown', 'n/a'):
                data[field] = '0'
            elif isinstance(value, str):
                # Problematic thousands separator with numeric fields.
                data[field] = value.replace(',', '')

        return super().to_internal_value(data)

    def create(self, validated_data):
        """Create instance as normal, but prevent duplication.
        """
        if not Starship.objects.filter(
            name=validated_data['name'],
            manufacturer=validated_data['manufacturer']
        ).exists():
            return super().create(validated_data)