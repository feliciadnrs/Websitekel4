from django.shortcuts import render, redirect, get_object_or_404
from .forms import HargaForm, POSForm, PrediksiForm, CountryForm, CustomerForm
from .models import Harga, POS, Prediksi,Customer, Country

def home(request):
    return render(request, 'home.html')

# Harga Views
def harga_list(request):
    hargas = Harga.objects.all()
    return render(request, 'harga_list.html', {'hargas': hargas})

def harga_create(request):
    if request.method == 'POST':
        form = HargaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('harga_list')
        else:
            print(form.errors) 
    else:
        form = HargaForm()
    return render(request, 'add_harga.html', {'form': form})

def harga_update(request, pk):
    harga = get_object_or_404(Harga, pk=pk)
    if request.method == 'POST':
        form = HargaForm(request.POST, instance=harga)
        if form.is_valid():
            form.save()
            return redirect('harga_list')
    else:
        form = HargaForm(instance=harga)
    return render(request, 'harga_form.html', {'form': form})

def harga_delete(request, pk):
    harga = get_object_or_404(Harga, pk=pk)
    if request.method == 'POST':
        harga.delete()
        return redirect('harga_list')
    return render(request, 'harga_confirm_delete.html', {'harga': harga})

# POS Views

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        else:
            print(form.errors)
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_form.html', {'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customer_confirm_delete.html', {'customer': customer})


def country_list(request):
    countries = Country.objects.all()
    return render(request, 'country_list.html', {'countries': countries})

def country_create(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('country_list')
        else:
            print(form.errors)
    else:
        form = CountryForm()
    return render(request, 'add_country.html', {'form': form})

def country_update(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country_list')
    else:
        form = CountryForm(instance=country)
    return render(request, 'country_form.html', {'form': form})

def country_delete(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        country.delete()
        return redirect('country_list')
    return render(request, 'country_confirm_delete.html', {'country': country})

def pos_list(request):
    poss = POS.objects.all()
    return render(request, 'pos_list.html', {'poss': poss})

def pos_create(request):
    if request.method == 'POST':
        form = POSForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pos_list')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = POSForm()
    return render(request, 'add_pos.html', {'form': form})
def pos_update(request, pk):
    pos = get_object_or_404(POS, pk=pk)
    if request.method == 'POST':
        form = POSForm(request.POST, instance=pos)
        if form.is_valid():
            form.save()
            return redirect('pos_list')
    else:
        form = POSForm(instance=pos)
    return render(request, 'pos_form.html', {'form': form})

def pos_delete(request, pk):
    pos = get_object_or_404(POS, pk=pk)
    if request.method == 'POST':
        pos.delete()
        return redirect('pos_list')
    return render(request, 'pos_confirm_delete.html', {'pos': pos})

# Prediksi View

# views.py

def prediksi_create(request):
    hasil_prediksi = None
    if request.method == 'POST':
        form = PrediksiForm(request.POST)
        if form.is_valid():
            # Lakukan prediksi atau simpan data di sini
            prediksi = form.save()
            hasil_prediksi = 'Customer akan kembali' if prediksi == 1 else 'Customer Tidak Kembali'  # Contoh sederhana, Anda bisa menambahkan logika prediksi di sini
    else:
        form = PrediksiForm()
    return render(request, 'prediksi_create.html', {'form': form, 'hasil_prediksi': hasil_prediksi})


import requests

def get_prediction(data):
    url = 'http://127.0.0.1:8000/predict'
    response = requests.post(url, json=data)
    return response.json()['prediction']
