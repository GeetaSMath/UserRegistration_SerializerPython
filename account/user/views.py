from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer
from .utility.token_gen import TokenGenerate

class Register(APIView):
    """
    This class register new user based on the details..
    """
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user=serializer.data
            token_gen =TokenGenerate.encode_token(self,user['username'],user['password'])

            return Response({'Message': 'user registered successfully', "data" : token_gen}, status=status.HTTP_201_CREATED)

        except ValueError as vrr:
            return Response({'Message':vrr.__str__()}, status=status.HTTP_400_BAD_REQUEST)

        except  ValidationError as exp:
            return Response({"Message":exp.__str__()},status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message':e.__str__()}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        """
        this method is created for retrieve data
        :param request: format of the request
        :return: Response
        """
        try:
            user = User.objects.all()
            serializer = UserSerializer(user,many=True)
            return Response({'Message' : 'data featched successfully',"data":serializer.data}, status=status.HTTP_201_CREATED)
        except ValueError as vrr:
            return Response({'Message':vrr.__str__()}, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as vde :
            return Response({'Message':vde.__str__()}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message':e.__str__()}, status=status.HTTP_400_BAD_REQUEST)


    def put (self, request, username):
        """
        put method to update data
        :param request:
        :param username:
        :return:
        """
        try:
            user = User.objects.get(username=username)
            user.password = request.data['password']
            user.email = request.data['email']
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.save()
            user_info = {"username": user.username, "password": user.password, "email": user.email,
                         "first_name": user.first_name, "last_name": user.last_name}

            return Response({"messages":'user updated',"data":user_info}, status=status.HTTP_201_CREATED)
        except ValueError as val:
            return Response({'Message':val.__str__()}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as vde:
            return Response({'Message':vde.__str__()}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Message': e.__str__()}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
        delete item with username
        :param request:
        :return:
        """
        try:
            user = User.objects.get(username=request.data['username'])
            user.delete()
            return Response({"deleted user": "done"}, status=status.HTTP_200_OK)
        except Exception as exe:
            return Response({"Message": exe.__str__()},status=status.HTTP_404_NOT_FOUND)

class Login(APIView):
    def post(self, request):
        """
        This method is created for user login
        :param request: web request for login the user
        :return:response
        """
        try:
            login_token = request.META['HTTP_TOKEN']
            decode = TokenGenerate.decode_token(self,login_token)
            if decode:
                return Response({"message": "login successfully"},
                                status=status.HTTP_200_OK)
            return Response({"message": "invalid user"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":e.__str__()},status=status.HTTP_400_BAD_REQUEST)


