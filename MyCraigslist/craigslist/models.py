from django.db import models

# Create your models here.

class Search(models.Model):
    searchField = models.CharField(max_length=500)
    createdTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.searchField)

    class Meta():
        verbose_name_plural = 'Searches '

