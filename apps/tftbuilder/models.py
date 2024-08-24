from django.db import models

class Classe(models.Model):
    nome = models.CharField(max_length=50)
    condicoes_ativacao = models.JSONField()
    imagem = models.ImageField(upload_to='classes/', blank=True, null=True)
    def __str__(self):
        return self.nome
    
class Campeao(models.Model):
    nome = models.CharField(max_length=50)
    custo = models.IntegerField()
    classes = models.ManyToManyField(Classe, related_name='campeoes')
    imagem = models.ImageField(upload_to='campeoes/', blank=True, null=True)
    def __str__(self):
        return self.nome
