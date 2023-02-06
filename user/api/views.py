from rest_framework.decorators import api_view
from user.api.serializers import Register

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
      serializer = Register(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return serializer.data
