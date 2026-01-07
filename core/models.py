from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    imagem = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True
    )
    autor =  models.ForeignKey( 
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if len(self.titulo) < 5:
            raise ValidationError('O titulo deve ter pelo menos 5 caracteres.')
    def __str__(self):
        return self.titulo