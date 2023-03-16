from django.contrib import admin
from spa.models import *
# Register your models here.


class AdminCustumer(admin.ModelAdmin):
    list_display = ['nama', 'no_hp', 'alamat', 'tgl', 'keterangan', 'kategori']
    search_fields = ['nama']
    list_filter = ['kategori']
    list_per_page = 5


admin.site.register(Custumer, AdminCustumer)
admin.site.register(Kategori)
