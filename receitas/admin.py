from django.contrib import admin
from.models import Receita

@admin.register(Receita)

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('title', 'categoria', 'created_at', 'updated_at', 'image_preview')
    search_fields = ('title', 'description', 'ingredients')
    list_filter = ('categoria', 'created_at')
    readonly_fields = ('created_at', 'updated_at', 'image_preview')

# Para mostrar a imagem no admin
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" />'
        return "Sem Imagem"
    image_preview.allow_tags = True
    image_preview.short_description = "Pré visualização"
