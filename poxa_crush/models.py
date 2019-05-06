from django.db import models

# Create your models here.
class Crush(models.Model): 
    signo_opcoes = [
        ('áries', 'áries'),
        ('touro', 'touro'), 
        ('gêmeos','gêmeos'),
        ('câncer', 'câncer'), 
        ('leão', 'leão'), 
        ('virgem', 'virgem'),
        ('libra', 'libra'), 
        ('escorpião', 'escorpião'), 
        ('sagitário', 'sagitário'), 
        ('capricórnio', 'capricórnio'), 
        ('aquários','aquário'), 
        ('peixes', 'peixes'),   
    ]

    def __str__(self):
        return self.nome


    nome=models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    data = models.DateField()
    signo = models.CharField(max_length=15, choices=signo_opcoes)
    qualidade = models.CharField(max_length=100)
    defeito = models.CharField(max_length=100, default='não está comigo')
    reciproco = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='', null=True)
    