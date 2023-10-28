from rest_framework import serializers, viewsets

from api.models import User, Dog, Elefant, Mouse, Monkey

dbs = {"base1": 1, "BASE2": 2}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CatSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=100)
    age = serializers.IntegerField()


class DogSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=100)
    age = serializers.IntegerField()


class ElefantSerializer(serializers.Serializer):
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


class MouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouse
        fields = '__all__'
        read_only_fields = ('id',)


# viewset

class MonkeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Monkey
        fields = ('name', 'color', 'age')

def multiple_of_ten(value):
    db_lower = value.lower()
    for k, v in dbs.items():
        if k.lower() == db_lower:
            return k

    raise serializers.ValidationError('Not a multiple of ten')


class DBValidationSerializer(serializers.Serializer):
    db = serializers.CharField(max_length=50)

    def validate_db(self, value):
        db_lower = value.lower()
        for k, v in dbs.items():
            if k.lower() == db_lower:
                return k

        raise serializers.ValidationError('Not a multiple of ten')