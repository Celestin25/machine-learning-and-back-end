from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Menu
from .serializers import MenuSerializer
from django.core.exceptions import ObjectDoesNotExist
import json

@csrf_exempt
@require_http_methods(["POST"])
def create_menu_item(request):
    try:
        data = json.loads(request.body)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Menu item created successfully", "menuItem": serializer.data}, status=201)
        return JsonResponse({"error": serializer.errors}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
@require_http_methods(["GET"])
def get_menu_items(request):
    try:
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
@require_http_methods(["PUT"])
def update_menu_item(request, item_id):
    try:
        data = json.loads(request.body)
        item = Menu.objects.get(item_id=item_id)
        serializer = MenuSerializer(item, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Menu item updated successfully", "menuItem": serializer.data}, status=200)
        return JsonResponse({"error": serializer.errors}, status=400)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Menu item not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_menu_item(request, item_id):
    try:
        item = Menu.objects.get(item_id=item_id)
        item.delete()
        return JsonResponse({"message": "Menu item deleted successfully"}, status=200)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Menu item not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
