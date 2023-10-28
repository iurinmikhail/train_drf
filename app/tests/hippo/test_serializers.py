from hippo.serializers import HippoSerializer


def test_valid_hippo_serializer():
    valid_serializer_data = {
        "name": "test",
        "color": "test",
        "age": 1,
    }
    serializer = HippoSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_hippo_serializer():
    invalid_serializer_data = {
        "name": "test",
        "color": "test",
    }
    serializer = HippoSerializer(data=invalid_serializer_data)
    assert not  serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {"age": ["This field is required."]}
