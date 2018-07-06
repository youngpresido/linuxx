from rest_framework import serializers
from .models import GoalStatus, ScrumyGoals,ScrumyUser
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

class ScrumyUserSerializer(serializers.HyperlinkedModelSerializer):
    # scrumygoals=serializers.HyperlinkedIdentityField(view_name="user-scrumygoals")
    password=serializers.CharField(write_only=True)    
    class Meta:
        model=ScrumyUser
        fields=('id','url','name','username','email','role','scrumygoals','password')
        depth=2


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
        
        # lookup_field='url'

        

class GoalStatuSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=GoalStatus
        fields=('url',"name","scrumygoal")
        depth=2


class ScrumyGoalSerializer(serializers.HyperlinkedModelSerializer):
    # status= serializers.PrimaryKeyRelatedField(read_only=True)
    user=serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    # status=serializers.PrimaryKeyRelatedField(read_only=True)
    # queryset=ScrumyGoals.objects.all()
    # sstatus=serializers.PrimaryKeyRelatedField(many=True,view_name="scrumygoal-detail")
    class Meta:
        model=ScrumyGoals
        
        fields=('url','id','title','task','date_created','date_updated','status','user')
        
    def create(self, validated_data):

        data = validated_data.copy()
        data['user'] = self.context['request'].user
        return super(ScrumyGoalSerializer, self).create(data)

    
    # def create(self, validated_data):
    #     user_id = validated_data.pop('user_id')
    #     album = ScrumyGoals.objects.create(**validated_data)
    #     for track_data in user_id:
    #         Track.objects.create(album=album, **track_data)
    #     return album



