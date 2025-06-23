from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def obtener_get(request):
    return Response({"message": "Hola SOY UNA PETICION GET"})

@api_view(['POST'])
def obtener_post(request):
    data = request.data
    return Response({"received": data})

@api_view(['GET', 'POST'])
def obtner_get_post(request):
    if request.method == 'GET':
        return Response({"message": "UN get"})
    elif request.method == 'POST':
        print("Datos:", request.data)
        return Response({"Datos": "POST Datos", "data": request.data})
