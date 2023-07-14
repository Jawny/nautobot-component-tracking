from nautobot.core.models.generics import BaseModel 
from django.db import models

class Components(BaseModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
