from django.db import models
import joblib
import pandas as pd

class Harga(models.Model):
    id_barang = models.IntegerField(primary_key=True)
    nama_barang = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama_barang



#UABHHH INI AJAAA
class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country_code = models.CharField(max_length=10)
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class POS(models.Model):
    customer = models.CharField(max_length=255)  # Changed from ForeignKey to CharField
    country = models.CharField(max_length=255)  # Changed from ForeignKey to CharField
    nama_barang = models.ForeignKey('Harga', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    @property
    def total_harga(self):
        return self.nama_barang.harga * self.quantity

    def __str__(self):
        return f"Order {self.id} - {self.customer}"



#PREDIKSIIII JANGAN DIGANGGUU (gua ganggu dikit ya :v - Dav)
class Prediksi(models.Model):    
    nama_barang = models.IntegerField()
    kuartal = models.IntegerField()
    date = models.IntegerField()
    gender_female = models.IntegerField()
    gender_male = models.IntegerField()
    region = models.IntegerField()
    reject_f = models.IntegerField()
    agent = models.IntegerField()
    range_mahal = models.IntegerField()
    range_murah = models.IntegerField()
    range_sedang = models.IntegerField()

    def __str__(self):
        model = joblib.load("decision_tree_model.pkl")
        data = {
            'Kuartal': [self.kuartal],
            'Date': [self.date],
            'Gender_Female': [self.gender_female],
            'Gender_Male': [self.gender_male],
            'Region': [self.region],
            'Reject_F': [self.reject_f],
            'Agent': [self.agent],
            'Range_mahal': [self.range_mahal],
            'Range_murah': [self.range_murah],
            'Range_sedang': [self.range_sedang],
            'Nama Barang': [self.nama_barang]
        }
        data_df = pd.DataFrame(data)

        # Make the prediction
        prediction = model.predict(data_df)[0]
        return prediction