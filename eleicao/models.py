from django.db import models

# Create your models here.
class Eleitor(models.Model):
    nome = models.CharField(max_length = 128)
    cpf= models.CharField(max_length = 12)

class Candidato(Eleitor):
    codigoCandidato = models.CharField(max_length = 5)

class Token(models.Model):
    codigoToken = models.CharField(max_length = 5)
    cpf = models.ForeignKey(Eleitor, null=False, blank=False)
    votou = models.BooleanField()

class Vaga(models.Model):
    codigoVaga = models.CharField(max_length = 5)
    vaga = models.CharField(max_length = 128)

class CandidatoVaga(models.Model):
    codigoCandidato = models.ForeignKey(Candidato, null=True, blank = True)
    codigoVaga = models.ForeignKey(Vaga, related_name='vaga_candidato', null = True, blank = True)

class Eleicao(models.Model):
    codigoEleicao = models.CharField(max_length = 5)
    dataInicio = models.DateTimeField(blank=True, null=True)    
    dataFim = models.DateTimeField(blank=True, null=True)
    codigoVaga = models.ForeignKey(Vaga, related_name='vaga_eleicao', null = True, blank = True)

class Urna(models.Model):
    codUrna = models.CharField(max_length = 5)
    codigoEleicao = models.ForeignKey(Eleicao, null = True, blank = True)
    codigoCandidato = models.ForeignKey(Candidato, related_name='candidato_urna', null= True, blank = True)