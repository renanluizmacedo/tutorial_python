from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if len(self.titulo) < 5:
            raise ValidationError('O titulo deve ter pelo menos 5 caracteres.')
    def __str__(self):
        return self.titulo