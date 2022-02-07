from django.db import IntegrityError
from rest_framework.authtoken import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers import serializer

from .models import UserDetails
from .serializer import UserDetailsSerializer

class Register(APIView):
    """
    This class register new user based on the details..
    """
    def post(self, request):
        try:
            serializer = UserDetailsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'Message': 'user registered successfully',"data":serializer.data}, status=status.HTTP_201_CREATED)

        except ValueError:
            return Response(ValueError, status=status.HTTP_400_BAD_REQUEST)

        except  ValidationError:
            return Response("Exception:Username already exists!")

        except Exception as e:
            return Response({'Exception': str(e)})


    def get(self, request):
        """
        this method is created for retrieve data
        :param request: format of the request
        :return: Response
        """
        try:
            user = UserDetails.objects.all()
            serializer = UserDetailsSerializer(user,many=True)
            return Response({'Message' : 'data featched successfully',"data":serializer.data}, status=status.HTTP_201_CREATED)
        except ValueError:
            return Response(ValueError, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError:
            return Response("Exception:Username already exists!")

        except Exception as e:
            return Response({'Exception': str(e)})

    def put (self, request, username):
        """
        put method to update data
        :param request:
        :param username:
        :return:
        """
        try:
            user = UserDetails.objects.get(username=username)
            user.password = request.data['password']
            user.email = request.data['email']
            user.city = request.data['city']
            user.state = request.data['state']
            user.save()
            return Response({"messages":'user updated',"data":serializer.data}, status=status.HTTP_201_CREATED)
        except ValueError:
            return Response(ValueError, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response("Exception:updated")
        except Exception as e:
            return Response({'Exception':str(e)})

    def delete(self, request):
        """
        delete item with username
        :param request:
        :return:
        """
        try:
            user = UserDetails.objects.get(username=request.data['username'])
            user.delete()
            return Response({"deleted user": "done"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)})