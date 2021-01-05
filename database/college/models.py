from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class College(models.Model):

        id = models.BigAutoField(
        primary_key=True,
        )

        name = models.CharField(
            max_length=200,
            unique=True,
            blank=False,
            null=False,
            verbose_name='College Name',
            validators=[
            MinLengthValidator(10)
            ]
        )

        code = models.IntegerField(
            verbose_name='College Code',
            blank=True,
            validators=[
                MinLengthValidator(6)
            ]
        )
    
        chairman = models.CharField(
            max_length=150,
            blank=False,
            verbose_name='Chairman'
        )

        established_on = models.DateField(
            auto_now_add=True,
            verbose_name='Established Name'
        )
    
