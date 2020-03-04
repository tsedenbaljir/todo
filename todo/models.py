from django.db import models
 
#
class Project(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return str(self.name)
# 
class Bed(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

    # Орны төрөл (байнгын болон яаралтай тусламж, үйлчилгээний)
    KIND_CHOICES = [
        ('surgery-or-abdomen', 'Дотор / Мэс засал'),
        ('maternity', 'Эх барих'),
        ('premature', 'Хүүхэд'),
        ('other', 'Бусад'),
    ]
    kind = models.CharField(max_length=20, choices=KIND_CHOICES)

    # Одоогийн тусгай зөвшөөрөлтэй ор
    current = models.PositiveIntegerField()

    # Шинээр санал болгож буй ор
    increment = models.PositiveIntegerField()

    # Санал болгож буй орны бууралт
    decrement = models.PositiveIntegerField()

    # Төсөл дууссаны дараах нийт ор
    final = models.PositiveIntegerField()

    def __str__(self):
        return str(self.kind)
