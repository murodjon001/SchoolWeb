from django.db import models

# Create your models here.
class Science(models.Model):
    science_name = models.CharField(max_length=25, blank=False,verbose_name="Fan nomi")
    slug = models.SlugField(max_length=25, verbose_name="Science name url", unique=True, help_text="To'ldirish shart emas! Avtomatik to'ldiriladi!")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)
        verbose_name =("Fan")
        verbose_name_plural =("Fanlar")

    def __str__(self) -> str:
        return self.science_name