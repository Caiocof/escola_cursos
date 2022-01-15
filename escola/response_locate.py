from rest_framework import status
from rest_framework.response import Response


def create_locate(serialize, request):
    if serialize.is_valid():
        serialize.save()
        response = Response(serialize.data, status=status.HTTP_201_CREATED)
        id = str(serialize.data['id'])
        response['Location'] = request.build_absolute_uri() + id
        return response
