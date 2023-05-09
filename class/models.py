from django.db import models
from teacher.models import Teacher
# Create your models here.

class Group(models.Model):
    group_NumberLetter = models.CharField(
        max_length=75, 
        blank=False,
        verbose_name="Sinf",
        help_text='1-"B" sinfi')
    class_curator = models.ForeignKey(
        Teacher, 
        on_delete=models.RESTRICT,
        verbose_name="Sinf rahbari"
        )
    description = models.TextField(blank=True,verbose_name="Sinf haqida ma'lumot")
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("-created",)
        verbose_name =("Sinf")
        verbose_name_plural =("Maktabdagi mavjud Sinflar")

    def __str__(self) -> str:
        return self.group_NumberLetter
