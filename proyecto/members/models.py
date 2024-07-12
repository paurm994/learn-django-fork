from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

  def __str__(self) -> str:
    return f"{self.id} - {self.firstname}, {self.lastname}"