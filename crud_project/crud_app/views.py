from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MobileSerializer
from .models import Mobile

@api_view(http_method_names=['POST'])
def create_api(request):
    if request.method == 'POST':
        serializer = MobileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET'])
def list_api(request):
    data = Mobile.objects.all()
    serializer = MobileSerializer(data, many=True)
    return Response(serializer.data)

@api_view(http_method_names=['PUT', 'PATCH', 'DELETE'])
def update_delete_api(request, pk):
    obj = Mobile.objects.get(pk=pk)
    if request.method == 'PUT':
        serializer = MobileSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)




