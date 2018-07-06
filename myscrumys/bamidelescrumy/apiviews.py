from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics,viewsets
from .models import GoalStatus, ScrumyGoals,ScrumyUser
from django.core import exceptions
from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators
from .serializers import ScrumyUserSerializer,ScrumyGoalSerializer, GoalStatuSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class ScrumyUserList(viewsets.ModelViewSet):
    queryset=ScrumyUser.objects.all()
    serializer_class=ScrumyUserSerializer
    authentication_classes=(TokenAuthentication,)
    permissions_classes=(IsAuthenticated,)
    # def validate_email(self,value):
    #     qs=ScrumyUser.objects.filter(email__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError("The email must be unique")
    #     return value
    # def validate_username(self,value):
    #     qs=ScrumyUser.objects.filter(username__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError("The username must be unique")
    #     return value
    # def validate_password(self, value):
    #     try:
    #         validate_password(value)
    #     except ValidationError as exc:
    #         raise serializers.ValidationError(str(exc))
    #     return value

    


    # def update(self, instance, **validated_data):
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.tagline = validated_data.get('tagline', instance.tagline)

    #     instance.save()

    #     password = validated_data.get('password', None)
    #     confirm_password = validated_data.get('confirm_password', None)

    #     if password:
    #         instance.set_password(password)
    #         instance.save()

    #     update_session_auth_hash(self.context.get('request'), instance)

    #     return instance
    # def scrumygoals(self,request,pk=None):
    #     scrumyuser=self.get_object()
    #     serializers=ScrumyGoalSerializer(scrumyuser.user.all(),context={'request':request},many=True)
    #     return serializers.data

    # def pre_save(self,obj):
    #     obj=self.request.user
    # def create(self, request):
    #     serializer = self.serializer_class(data=request.data)

    #     if serializer.is_valid():
    #         ScrumyUser.objects.create_user(**serializer.validated_data)

    #         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    #     return Response({
    #         'status': 'Bad request',
    #         'message': 'Account could not be created with received data.'
    #     }, status=status.HTTP_400_BAD_REQUEST)

   

class ScrumyGoalsList(viewsets.ModelViewSet):
    queryset=ScrumyGoals.objects.all()
    serializer_class=ScrumyGoalSerializer
    authentication_classes=(TokenAuthentication,)
    permissions_classes=(IsAuthenticated,)
    # def pre_save(self,request,format=None):
    #     serializer=ScrumyGoalSerializer(data=request.data)
    #     if serializer.is_valid():
    #         temp=self.get_object(pk=int(self.request.data['status']))
    #         print(temp)
    #         serializer.save(status=temp)
    #         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)            
    #     return Response({
    #         'status': 'Bad request',
    #         'message': 'Account could not be created with received data.'
    #     }, status=status.HTTP_400_BAD_REQUEST)




class GoalStatusList(viewsets.ModelViewSet):
    queryset=GoalStatus.objects.all()
    serializer_class=GoalStatuSerializer
    authentication_classes=(TokenAuthentication,)
    permissions_classes=(IsAuthenticated,)