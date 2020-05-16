from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Pet, Appointment
from .forms import PetForm, AppointmentForm
from django.utils import timezone



def index(request):
    return render(request, 'pet_app/index.html')

class PetListView(LoginRequiredMixin, ListView):
    """ Renders a list of all Users pets. """
    login_url = reverse_lazy('login')
    model = Pet

    def get(self, request):
        """GET a list of pets."""
        context = {
            'pets': self.get_queryset().filter(owner=request.user),
            'form': PetForm(request.POST)
        }
        return render(request, 'pet_app/pet_list.html', context)

    def post(self, request):
        """Add a new pet."""
        form = PetForm(request.POST)
        if form.is_valid:
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            messages.success(request, f'{pet.pet_name} Added')
        else:
            messages.error(request, 'Could not add your pet.')
        context = {
            'pets': self.get_queryset().filter(owner=request.user),
            'form': form,
        }
        return render(request, 'pet_app/pet_list.html', context)


class PetDetailView(LoginRequiredMixin, DetailView):
    """ Renders a specific page based on it's slug."""
    login_url = reverse_lazy('login')
    model = Pet

    def get(self, request, pet_id):
        """ Returns a specific wiki page by slug. """
        context = {
          'pet': self.get_queryset().get(id=pet_id),
          'appointments': Appointment.objects.filter(pet__id=pet_id)
        }
        return render(request, 'pet_app/pet_detail.html', context)


class AppointmentListView(LoginRequiredMixin, ListView):
    """ Renders a list of all Users Appointments. """
    login_url = reverse_lazy('login')
    model = Appointment

    def get(self, request):
        """GET a list of appointment."""
        context = {
            'appointments': self.get_queryset().filter(
                        date_of_appointment__gte=timezone.now()
                        ).filter(pet__owner=request.user).order_by('date_of_appointment'),
            'form': AppointmentForm(request.POST)
        }
        return render(request, 'pet_app/appointment_list.html', context)

    def post(self, request):
        """Add a new Appointment."""
        form = AppointmentForm(request.POST)
        if form.is_valid:
            appointment = form.save(commit=False)
            appointment.save()
            messages.success(request, 'Added Appointment')
        else:
            messages.error(request, 'Appointment could not be saved')
        context = {
            'appointments': self.get_queryset().filter(
                        date_of_appointment__gte=timezone.now()
                        ).filter(pet__owner=request.user).order_by('date_of_appointment'),
            'form': form,
        }
        return render(request, 'pet_app/appointment_list.html', context)
