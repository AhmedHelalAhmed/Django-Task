from django.db import models
from django.core.validators import RegexValidator


class Patient(models.Model):
    patient_name = models.CharField(max_length=33)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Mobile must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    def __str__(self):
        return self.patient_name


class Visit(models.Model):
    visit_time = models.DateTimeField()
    visit_patient = models.ForeignKey(Patient)
    visit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.visit_time


class Order(models.Model):
    order_visit = models.ForeignKey(Visit)
    order_price = models.DecimalField(max_digits=6, decimal_places=2)
