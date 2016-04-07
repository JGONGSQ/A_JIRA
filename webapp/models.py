from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseDataModel(models.Model):
    def get_field_names(self):
        return [field.name for field in self._meta.fields]

    def get_values(self):
        return [getattr(self, field) for field in self.get_field_names()]

    class Meta:
        abstract = True


class Issue(BaseDataModel):
    """
    Register Issue Information
    """
    TYPE_BUG = 'BUG'
    TYPE_IMPROVEMENT = 'IMPROVEMENT'
    TYPE_TASK = 'TASK'

    TYPE = (
        (TYPE_BUG, 'BUG'),
        (TYPE_IMPROVEMENT, 'IMPROVEMENT'),
        (TYPE_TASK, 'TASK'),
    )

    user = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    type = models.CharField(max_length=64, choices=TYPE, default=TYPE_TASK)
    summary = models.TextField()
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
