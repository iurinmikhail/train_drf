from api.serializers import MouseSerializer


def test_mouse_serializer_valid():
    valid_serializer_data = {
        "name": "test",
        "color": "test",
        "age": 1
    }
    serializer = MouseSerializer(data=valid_serializer_data)
    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}

def test_invalid_mouse_serializer():
    invalid_serializer_data = {
        "name": "test",
        "color": "test",
        "age": "test"
    }
    serializer = MouseSerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    assert serializer.errors == {
        "age": [
            "A valid integer is required."
        ]
    }
