from rest_framework import serializers

from api.models import User, Dog, Elefant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CatSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=100)
    age = serializers.IntegerField()


class DogSerialise(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=100)
    age = serializers.IntegerField()


class ElefantSerialise(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return Elefant.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.color = validated_data.get('color', instance.color)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance