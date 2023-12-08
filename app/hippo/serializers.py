from rest_framework import serializers

from .models import Hippo


class HippoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hippo
        fields = "__all__"
        read_only_fields = ("id",)


class CheckSerializer(serializers.Serializer):
    instance_rids = serializers.ListField(
        child=serializers.IntegerField(), allow_empty=False
    )
