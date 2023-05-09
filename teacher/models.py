from django.db import models
from science.models import Science
# Create your models here.
class Position(models.Model):
    position = models.CharField(max_length=50, verbose_name='Lavozim')
    is_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)
        verbose_name =("Lavozim")
        verbose_name_plural =("Maktab ma'muriyatidagi lavozimlar")

    def __str__(self) -> str:
        return self.position


class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ism Familya",blank=False)
    phone = models.CharField(max_length=13, verbose_name='Telefon raqam', blank=False)
    photo = models.ImageField(upload_to="images/", verbose_name="Rasm")
    position = models.ForeignKey(Position, on_delete=models.RESTRICT,blank=True, null=True, verbose_name="Lavozim")
    science = models.ForeignKey(Science, on_delete=models.RESTRICT, blank=False, verbose_name='Mutaxassislik')
    description = models.TextField(blank=False, verbose_name="Tarjimai hol")
    is_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)
        verbose_name =("Maktab o'qituvchisi")
        verbose_name_plural =("Maktab o'qituvchilari")

    def __str__(self) -> str:
        return self.name


class SchoolAdministration(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ism Familya",blank=False)
    phone = models.CharField(max_length=13, verbose_name='Telefon raqam', blank=False)
    photo = models.ImageField(upload_to="images/", verbose_name="Rasm")
    position = models.ForeignKey(Position, on_delete=models.RESTRICT, verbose_name="Lavozim")
    science = models.ForeignKey(Science, on_delete=models.RESTRICT, blank=True,null=True, verbose_name='Mutaxassislik',help_text="Ixtiyoriy")
    description = models.TextField(blank=False, verbose_name="Tarjimai hol")
    is_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)
        verbose_name =("Maktab ma'muriyati")
        verbose_name_plural =("Maktab ma'muriyati")

    def __str__(self) -> str:
        return self.name