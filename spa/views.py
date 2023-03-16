from django.shortcuts import render, redirect
from spa.forms import FormCustumer
from spa.models import *
from django.contrib  import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def index(request):
    if request.POST:
        form = FormCustumer(request.POST)
        if form.is_valid():
            form.save()
            form = FormCustumer()
            pesan = "Berhasil order"
            messages.warning(request, 'Berhasil order')

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return redirect('/')
    else:
        form = FormCustumer()

    konteks = {
        'form': form,
    }

    return render(request, 'index.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def service(request):
    return render(request, 'service.html')

@login_required(login_url=settings.LOGIN_URL)
def ubah_custumer(request, id_custumer):
    custumer = Custumer.objects.get(id=id_custumer)
    if request.POST:
        form = FormCustumer(request.POST, instance=custumer)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Diperbarui")
            return redirect('ubah-custumer', id_custumer=id_custumer)
    else:
        form = FormCustumer(instance=custumer)
        konteks = {
            'form': form,
            'custumer': custumer,
        }
        return render(request,'ubah-custumer.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def custumer(request):
    custumer = Custumer.objects.all()

    konteks = {
        'custumer': custumer,
    }
    return render(request, 'custumer.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_custumer(request):
    if request.POST:
        form = FormCustumer(request.POST)
        if form.is_valid():
            form.save()
            form = FormCustumer()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-custumer.html', konteks)
    else:
        form = FormCustumer()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-custumer.html', konteks)
