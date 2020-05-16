from django.test import TestCase
from .models import Pet, Appointment
from django.utils import timezone
from django.contrib.auth.models import User

# Test Page List Page
# Creates the user and pet objects
# Checks if pet is in result

class PetsListTestCase(TestCase):
	def test_pets_list_page(self):
		mondale = User()
		mondale.save()
		pet = Pet()
		pet.owner = mondale
		pet.pet_name = "Jimmy"
		pet.species = "Llama"
		pet.breed = "Some horse"
		pet.weight_in_pounds = 1000
		pet.save()
		self.client.force_login(mondale)
		response = self.client.get("/pets/")
		self.assertContains(response,"Jimmy")
		


class PetsDetailTestCase(TestCase):
	def test_pet_detail_page(self):
		mondale = User()
		mondale.save()

		pet = Pet()
		pet.owner = mondale
		pet.pet_name = "Jimmy"
		pet.species = "Llama"
		pet.breed = "Some horse"
		pet.weight_in_pounds = 1000
		pet.save()

		appointment = Appointment()
		appointment.date_of_appointment = timezone.now()
		appointment.duration_minutes = 1000
		appointment.special_instructions = "Love him"
		appointment.pet = pet
		appointment.save()
		self.client.force_login(mondale)

		response = self.client.get(f"/pets/{pet.id}/")
		self.assertContains(response, "Jimmy")



class PetCreationTestCase(TestCase):
	def test_add_pet(self):
		mondale = User()
		mondale.save()
		pet_context = {
			"pet_name" : "Jimmy",
			"species" : "Llama",
			"breed" : "Horse thing",
			"weight_in_pounds" : 1000
		}
		self.client.force_login(mondale)
		response = self.client.post("/pets/", pet_context)
		pet = Pet.objects.get(pet_name="Jimmy")
		self.assertEqual(pet.pet_name,"Jimmy")













