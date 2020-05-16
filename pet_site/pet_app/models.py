from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):

	pet_name = models.CharField(max_length=100, help_text="Pet Name")
	species = models.CharField(max_length=50, help_text="Species")
	breed = models.CharField(max_length=50, help_text="Breed")
	weight_in_pounds = models.IntegerField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Pet Owner")

	def __str__(self):
		return str(self.pet_name)


class Appointment(models.Model):

	pet = models.ForeignKey(Pet, on_delete=models.CASCADE, help_text="Pet that the appointment is for.")
	date_of_appointment = models.DateField()
	duration_minutes = models.IntegerField()
	special_instructions = models.TextField()