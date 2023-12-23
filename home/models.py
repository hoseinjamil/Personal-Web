from django.db import models


class ContactMe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    body = models.CharField(max_length=500)


    def __str__(self):
        return self.subject
