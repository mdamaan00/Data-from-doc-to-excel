from django.db import models
from django.db.models.deletion import CASCADE


class Document(models.Model):
    docfile = models.FileField(upload_to='documents_other/')



class Excel(models.Model):
    docfile = models.FileField(upload_to='documents_excel/')

class Pdf(models.Model):
    excel = models.ForeignKey(Excel,on_delete=models.CASCADE,default=None)
    docfile = models.FileField(upload_to='documents_pdf/')