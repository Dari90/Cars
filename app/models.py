from django.db import models

class Cars(models.Model):

    MECHANIC = 1
    AUTOMATIC = 2
    ROBOTIC = 3

    TRANSMISSION_TYPE = [
        (MECHANIC, "механика"),
        (AUTOMATIC, "автомат"),
        (ROBOTIC, "робот"),
    ]

    model = models.CharField(verbose_name = "Model", max_length=50)
    manufacturer = models.CharField(verbose_name = "Manufacturer", max_length=50)
    transmission = models.SmallIntegerField(verbose_name = "Transmission", choices=TRANSMISSION_TYPE, default=0)
    release_year = models.IntegerField(verbose_name = "Release year")
    colors = models.CharField(verbose_name = "Color", max_length=30)
    photo = models.ImageField(verbose_name='Photo', upload_to='photos', blank=True)

    class Meta:
        verbose_name = u"Автомобиль"
        verbose_name_plural = u"Автомобили"

    def __str__(self):
        return f'{self.manufacturer} {self.model}'
