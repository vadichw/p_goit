from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Note(models.Model):
    objects = None
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150, null=False)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag) # За допомогою інструкції tags = models.ManyToManyField(Tag) ми створюємо зв'язок багато-до-багатьох між нотатками та тегами.

    def __str__(self):
        return f"{self.name}"
