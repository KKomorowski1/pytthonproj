from django.db import models


# Create your models here.


class General(models.Model):
    producent = models.CharField(max_length=200, null=False, blank=False)
    typ = models.CharField(max_length=200, unique=True)


class Details(models.Model):
    general = models.ForeignKey(General, on_delete=models.CASCADE)
    procesor = models.CharField(max_length=200, default='Brak Informacji', null=False, blank=False)
    pamiec = models.CharField(max_length=200, default='Brak Informacji', null=False, blank=False)
    pamiec_ram = models.CharField(max_length=200, default='Brak Informacji', null=False, blank=False)
    bateria = models.CharField(max_length=200, default='Brak Informacji', null=False, blank=False)

    def __str__(self):
        return '{}{}{}{}'.format(self.procesor, self.pamiec, self.pamiec_ram, self.bateria)
