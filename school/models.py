from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name="Ism Familya")
    phone = models.CharField(max_length=13, blank=False, verbose_name="Telefon raqam")
    description = models.TextField(blank=True, verbose_name="messages")
    data_create = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("-data_create",)
        verbose_name =("Bildirishnoma")
        verbose_name_plural =("Bildirishnomalar")

    def __str__(self) -> str:
        return self.name