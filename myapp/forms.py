from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Harga, POS, Prediksi,Customer,Country
from .models import POS

class HargaForm(forms.ModelForm):
    class Meta:
        model = Harga
        fields = ['id_barang', 'nama_barang', 'harga']
    
    def clean_id_barang(self):
        id_barang = self.cleaned_data.get('id_barang')
        if Harga.objects.filter(id_barang=id_barang).exists():
            raise forms.ValidationError('ID Barang already exists. Please enter a unique ID.')
        return id_barang

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))


#UBAH DARI SINI
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_id', 'name', 'company', 'address', 'gender', 'email', 'phone']

    def clean_customer_id(self):
        customer_id = self.cleaned_data.get('customer_id')
        if Customer.objects.filter(customer_id=customer_id).exists():
            raise forms.ValidationError('Customer ID already exists. Please enter a unique ID.')
        return customer_id

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country_id', 'country_code', 'country_name']

    def clean_country_id(self):
        country_id = self.cleaned_data.get('country_id')
        if Country.objects.filter(country_id=country_id).exists():
            raise forms.ValidationError('Country ID already exists. Please enter a unique ID.')
        return country_id

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class POSForm(forms.ModelForm):
    class Meta:
        model = POS
        fields = ['customer', 'country', 'nama_barang', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

#JGN DIGANGGU
class PrediksiForm(forms.ModelForm):
    class Meta:
        model = Prediksi
        fields = '__all__'