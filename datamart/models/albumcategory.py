from django.db import models


class AlbumCategory(models.Model):
    category_name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category_name }"

    class Meta:
        verbose_name = 'Album Category'
        verbose_name_plural = 'Album Categories'