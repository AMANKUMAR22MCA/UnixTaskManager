from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)

#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             response = Response()
#             response.set_cookie("access", str(refresh.access_token), httponly=True)
#             response.set_cookie("refresh", str(refresh), httponly=True)
#             response.data = {
#                 "message": "Logged in successfully",
#                 "access": str(refresh.access_token),
#                 "refresh": str(refresh)
#             }
#             return response
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class LoginView(APIView):
    def post(self, request):
        # Retrieve username and password from the request
        username = request.data.get("username")
        password = request.data.get("password")

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Generate refresh and access tokens using Simple JWT
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Send the tokens in the response
            response = Response({
                "message": "Login successful",
                "access": access_token,
                "refresh": refresh_token,
            })

            # Optionally, set tokens in cookies (If you want)
            # response.set_cookie("access", access_token, httponly=True)
            # response.set_cookie("refresh", refresh_token, httponly=True)

            return response
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        response.data = {"message": "Logged out successfully"}
        return response

class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })

