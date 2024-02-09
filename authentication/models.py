from django.db import models

class Coroa(models.Model):
    data = models.CharField(max_length=255)
    código = models.CharField(max_length=255)
    lote = models.CharField(max_length=255)
    número = models.CharField(max_length=255)
    colo_superior = models.CharField(max_length=255)
    colo_inferior = models.CharField(max_length=255)
    furo_anel = models.CharField(max_length=255)
    folga_anel = models.CharField(max_length=255)
    encaixe_co_bl = models.CharField(max_length=255)
    externo = models.CharField(max_length=255)
    situacao_final = models.CharField(max_length=255)
    colaborador = models.CharField(max_length=255)
    
 
class Forma(models.Model):
    data = models.CharField(max_length=255)
    código = models.CharField(max_length=255)
    lote = models.CharField(max_length=255)
    número = models.CharField(max_length=255)
    colo = models.CharField(max_length=255)
    pescoco = models.CharField(max_length=255)
    ombro = models.CharField(max_length=255)
    calcanhar = models.CharField(max_length=255)
    rodape = models.CharField(max_length=255)
    flexa = models.CharField(max_length=255)
    furo_de_escape = models.CharField(max_length=255)
    encaixe_ffo = models.CharField(max_length=255)
    externo = models.CharField(max_length=255)
    situacao_final = models.CharField(max_length=255)
    colaborador = models.CharField(max_length=255)
    

class Bloco(models.Model):
    data = models.CharField(max_length=255)
    código = models.CharField(max_length=255)
    lote = models.CharField(max_length=255)
    número = models.CharField(max_length=255)
    colo = models.CharField(max_length=255)
    rodape = models.CharField(max_length=255)
    flexa = models.CharField(max_length=255)
    encaixe_angular = models.CharField(max_length=255)
    encaixe_fb = models.CharField(max_length=255)
    externo = models.CharField(max_length=255)
    situacao_final = models.CharField(max_length=255)
    colaborador = models.CharField(max_length=255)
    
    