from django.db import models

# Create your models here.


class WebService(models.Model):
    id = models.IntegerField('ID', primary_key=True, unique=True, null=False)
    name = models.CharField('name', max_length=255, unique=True, null=False)
    url = models.CharField('URL', max_length=255, unique=True, null=False)
    is_deleted = models.BooleanField('is_deleted', null=False)

    def __str__(self):
        return self.id


class Parameter(models.Model):
    id = models.IntegerField('ID', primary_key=True, unique=True, null=False)
    name = models.CharField('name', max_length=255, unique=True, null=False)
    value = models.CharField('value', max_length=255, unique=True, null=False)
    generic_param = models.ForeignKey('GenericParameter')
    web_service = models.ForeignKey('WebService')
    is_deleted = models.BooleanField('is_deleted', null=False)

    def __str__(self):
        return self.id


class GenericParameter(models.Model):
    id = models.IntegerField('ID', primary_key=True, unique=True, null=False)
    param = models.CharField('param', max_length=255, unique=True, null=False)
    value = models.CharField('value',  max_length=255, unique=True, null=False)
    is_deleted = models.BooleanField('is_deleted', null=False)

    def __str__(self):
        return self.id