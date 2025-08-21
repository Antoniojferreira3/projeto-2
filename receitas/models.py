from django.db import models

class Receita(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    #campo para imagem da receita
    image = models.ImageField(upload_to='receitas_images/', blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        ordering = ['-created_at']# ordena as receitas pela data de criação, da mais recente para a mais antiga
