from django.db import models


class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    index_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
