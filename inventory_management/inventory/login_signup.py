from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from rest_framework import status
import jwt
class loginSignUp(APIView):
    def post(self, request):
        email=request.data.get('email')
        name=request.data.get('name')
        password=request.data.get('password')

        is_user_exists=models.users.objects.filter(email=email).exists()

        if is_user_exists:
            user_details=models.users.objects.filter(email=email, password=password).first()
        else:
            user_details=models.users.objects.create(email=email,name=name,password=password)
        if user_details:
            token={
                'id':user_details.id,
                'email':user_details.email,
                'name':user_details.name
            }
            jwt_token=jwt.encode(token, 'user key', algorithm='HS256')
            return Response({'token':jwt_token},status=status.HTTP_200_OK)
        else:
                return Response({'data':'Invalid Password'},status=status.HTTP_400_BAD_REQUEST)
