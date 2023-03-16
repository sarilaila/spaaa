from django.forms import ModelForm
from django import forms
from spa.models import *


class FormCustumer(ModelForm):
    class Meta:
        model = Custumer
        fields = '__all__'

        widgets = {
            'Nama': forms.TextInput({'class':'form-control'}),
            'Nomer HP': forms.TextInput({'class':'form-control'}),
            'Alamat': forms.TextInput({'class':'form-control'}),
            'Tanggal': forms.TextInput({'class':'form-control'}),
            'Keterangan': forms.TextInput({'class':'form-control'}),
            'Kategori': forms.TextInput({'class':'form-control'}),
        }
