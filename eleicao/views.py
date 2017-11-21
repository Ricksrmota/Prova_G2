from django.shortcuts import render
from eleicao.serializers import *

# Create your views here.

class EleitorViewSet(viewsets.ModelViewSet):
    queryset = Eleitor.objects.all()
    serializer_class = EleitorSerializer

class EleicaoViewSet(viewsets.ModelViewSet):
    queryset = Eleicao.objects.all()
    serializer_class = EleicaoSerializer

class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
    
class UrnaViewSet(viewsets.ModelViewSet):
    queryset = Urna.objects.all()
    serializer_class = UrnaSerializer