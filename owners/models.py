from django.db import models

class Owner(models.Model):
    name  = models.CharField(max_length=45, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    age   = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
            db_table = 'owners'

class Dog(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    name  = models.CharField(max_length=45, null=True, blank=True)
    age   = models.PositiveSmallIntegerField(null=True, blank=True)
	
    class Meta:
            db_table = 'dogs'
