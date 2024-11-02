from rest_framework.decorators import api_view
from rest_framework.response import Response 

def getRoutes(request):
    routes=[
        'GET /api/romms',
        'GET /api/room/:id'
    ]
    return JsonResponse(routes,safe=False)
