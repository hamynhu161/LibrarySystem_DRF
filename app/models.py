from django.db import models

class Kirja(models.Model):
    otsikko = models.CharField(max_length=100, default='')
    kirjoittaja = models.CharField(max_length=50, default='')
    isbn = models.CharField(max_length=13, default='')
    saatavissa = models.BooleanField(default=True)

    class Meta:                     
        ordering = ['otsikko']     

    def __str__(self):
        return f"{self.otsikko} by {self.kirjoittaja}"    

class Asiakas(models.Model):
    nimi = models.CharField(max_length=100, default='')
    puhelin = models.CharField(max_length=20, default='')
    email = models.EmailField()

    class Meta:
        ordering = ['nimi']

    def __str__(self):
        return self.nimi

class Lainaus(models.Model):
    kirja = models.ForeignKey(Kirja, on_delete=models.CASCADE)
    asiakas = models.ForeignKey(Asiakas, on_delete=models.CASCADE)
    lainattu_aika = models.DateTimeField()
    palautettu_aika = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['kirja']


    def save(self, *args, **kwargs):
    # Jos laina on aktiivinen (ei palautettu), merkitse kirja ei-saatavilla olevaksi
        if self.palautettu_aika is None:
            self.kirja.saatavissa = False
        else:
            self.kirja.saatavissa = True
        self.kirja.save() 
        super().save(*args, **kwargs) # Tallenna itse laina

    def delete(self, *args, **kwargs):
        # Jos laina on poistettu, merkitse kirja saatavilla olevaksi
        self.kirja.saatavissa = True
        self.kirja.save()
        super().delete(*args, **kwargs)