from django.test import TestCase
from django.urls import reverse
from .models import Esporte, Time

class EsporteTestCase(TestCase):
    def setUp(self):
        self.esporte = Esporte.objects.create(nome_esporte="Futebol")

    def test_esporte_creation(self):
        esporte = Esporte.objects.get(nome_esporte="Futebol")
        self.assertEqual(esporte.nome_esporte, "Futebol")

    def test_esporte_str_representation(self):
        self.assertEqual(str(self.esporte), "Futebol")


class TimeTestCase(TestCase):
    def setUp(self):
        self.esporte = Esporte.objects.create(nome_esporte="Basquete")
        self.time = Time.objects.create(nome_time="Time A", nome_esporte=self.esporte)

    def test_time_creation(self):
        time = Time.objects.get(nome_time="Time A")
        self.assertEqual(time.nome_time, "Time A")
        self.assertEqual(time.nome_esporte, self.esporte)

    def test_time_str_representation(self):
        self.assertEqual(str(self.time), "Time A")
