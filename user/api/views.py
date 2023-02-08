from rest_framework.decorators import api_view
from user.api.serializers import Register
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user.api.models import create_auth_token

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
      serializer = Register(data=request.data)

      data = {}

      if serializer.is_valid():
          account = serializer.save()

          data['response'] = "Registration succesful"
          data['username'] = account.username
          data['email'] = account.email

          token = Token.objects.get(user=account).key
          data['token'] = token

      else:
          data = serializer.errors

      return Response(data)
