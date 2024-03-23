from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email',
    ordering = '-id',
    # list_filter = 'first_name',
    search_fields = 'first_name', 'phone',
    list_per_page = 5 #quantas linhas serão exibidas
    list_max_show_all = 30 #quantidade máxima de linhas que serão exibidas caso clicar em mostrar tudo
    #list_editable = 'phone', 'email', permite editar informações vinculadas nessa tupla
    list_display_links = 'first_name', 'last_name',