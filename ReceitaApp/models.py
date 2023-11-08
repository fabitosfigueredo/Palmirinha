from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return(self.nome)

GRAUS_DE_DIFICULDADES =[
     ('F', 'Fácil'),
     ('M', 'Moderado'),
     ('D', 'Dificil')
     ]



class Receita(models.Model):
    nome = models.CharField(max_length=50)
    ingredientes = models.TextField(max_length=2000)
    modo_de_preparo = models.TextField(max_length=8000)
    grau_de_dificuldade = models.CharField(max_length=10,choices=GRAUS_DE_DIFICULDADES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return(self.nome)