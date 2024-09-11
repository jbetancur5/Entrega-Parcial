from django.shortcuts import render, redirect
from django.db.models import Avg
from .forms import FlightForm
from .models import Flight

def register_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_flights')
    else:
        form = FlightForm()
    return render(request, 'register_flight.html', {'form': form})

def list_flights(request):
    flights = Flight.objects.all().order_by('price')
    return render(request, 'list_flights.html', {'flights': flights})


def flight_stats(request):
    national_flights = Flight.objects.filter(flight_type='Nacional').count()
    international_flights = Flight.objects.filter(flight_type='Internacional').count()
    avg_national_price = Flight.objects.filter(flight_type='Nacional').aggregate(avg_price=Avg('price'))['avg_price']
    return render(request, 'flight_stats.html', {
        'national_flights': national_flights,
        'international_flights': international_flights,
        'avg_national_price': avg_national_price
    })