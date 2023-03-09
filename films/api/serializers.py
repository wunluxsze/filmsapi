from rest_framework import serializers
from .models import Director
from .models import Films
from .models import Genre
from .models import Afisha


class DerictorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"

class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class AfishaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afisha
        fields = "__all__"