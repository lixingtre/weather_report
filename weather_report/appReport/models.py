from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class City_master(models.Model):
    city_id = models.TextField(
        primary_key=True,
        verbose_name="City",
        unique=True,
        max_length=50,
        validators=[
            RegexValidator(
                regex="^[A-Za-z0-9_]+$", message="please input numbers and letters", code="nomatch"
            )
        ],
    )
    country = models.TextField(verbose_name="Country", max_length=50)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = "city_master"
        verbose_name = "cities"
        verbose_name_plural = "weather information of city"

class City_weather(models.Model):
    city = models.ForeignKey(
        City_master,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="City",
    )

    weather_information = models.TextField(verbose_name="weather information of city", max_length=500)
    date = models.DateField(auto_now_add=True, verbose_name="Date")
    

    def __str__(self):
        return self.user_id + "_" + self.user_name

    class Meta:
        db_table = "weather_report"
        verbose_name = "cities"
        verbose_name_plural = "weather information of city"