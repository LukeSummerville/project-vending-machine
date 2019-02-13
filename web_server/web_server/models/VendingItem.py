from django.db import models

class VendingItem(models.Model):
    # TODO add fields
    #id: int
    #name: string
    #description: string
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
