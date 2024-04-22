from django.views.generic import ListView
from django.shortcuts import render
from django.utils.decorators import method_decorator  # Fix for NameError
from django.views.decorators.csrf import csrf_exempt  # Fix for NameError
from mapAdminApp.models import Locations
from django.views import View
from django.http import JsonResponse  # To return JSON responses
from .models import Locations  # Importing the correct model
import json  # For handling JSON data





# Create your views here.
class HomeView(ListView):
    template_name = "mapAdminApp/home.html"
    context_object_name = 'locations'  # This matches with your template
    model = Locations


@method_decorator(csrf_exempt, name='dispatch')
class GeolocationView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)  # Parse the JSON request body
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            # Create and save a new Location instance
            new_location = Locations(latitude=latitude, longitude=longitude)  # Use correct model name
            new_location.save()

            return JsonResponse({"status": "success"}, status=201)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
        




