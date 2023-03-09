from rest_framework.response import Response
from rest_framework import status
from .models import Films
from .models import Director
from .models import Afisha
from .models import Genre
from .serializers import FilmsSerializer
from .serializers import DerictorSerializers
from .serializers import AfishaSerializer
from .serializers import GenreSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView


class FilmsList(ListAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer


class FilmsCRUD(RetrieveUpdateDestroyAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer

class DirectorList(ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DerictorSerializers


class DirectorCRUD(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DerictorSerializers


class AfishaList(ListAPIView):
    queryset = Afisha.objects.all()
    serializer_class = AfishaSerializer


class AfishaCRUD(RetrieveUpdateDestroyAPIView):
    queryset = Afisha.objects.all()
    serializer_class = AfishaSerializer


class GenreList(ListAPIView):
    queryset = Director.objects.all()
    serializer_class = GenreSerializer


class GenreCRUD(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
