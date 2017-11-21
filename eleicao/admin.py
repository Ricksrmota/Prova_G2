from django.contrib import admin
from eleicao.models import *

# Register your models here.
Eleitor, Candidato, Token, Vaga, CandidatoVaga, Eleicao, Urna
admin.site.register(Eleitor)
admin.site.register(Candidato)
admin.site.register(Vaga)
admin.site.register(Token)
admin.site.register(CandidatoVaga)
admin.site.register(Eleicao)
admin.site.register(Urna)

