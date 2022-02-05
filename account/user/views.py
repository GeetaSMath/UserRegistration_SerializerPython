from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserDetailsSerializer
from .models import UserDetails


class Register(APIView):
    """
    This class register new user based on the details..
    """
    def post(self, request):
        try:
            serializer = UserDetailsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'Message': 'user registered successfully'}, status=status.HTTP_201_CREATED)

        except ValueError:
            return Response(ValueError, status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError:
            return Response("Exception:Username already exists!")

        except Exception as e:
            return Response({'Exception': str(e)})