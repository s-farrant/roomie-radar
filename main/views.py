from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.utils.timezone import now

from .models import Roomie

@csrf_exempt
def update_status(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            status = data.get("status")

            if (name is None) or (status is None):
                return JsonResponse({"error": "Bad request"}, status=400)
            
            obj, created = Roomie.objects.update_or_create(
                name=name,
                defaults={
                    'status': status,
                    'updated_at': now()
                }
            )
            return JsonResponse({"message": "Status updated", "created": created})
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
    return JsonResponse({"error": "Only POST requests allowed"}, status=405)


def home_status(request):
    roomies = Roomie.objects.all().order_by("name")
    return render(request, "main/home.html", {"roomies": roomies})