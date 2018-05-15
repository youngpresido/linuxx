from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from .views import ScrumyUser

class EmailAuthBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            user=ScrumyUser.objects.get(username=username)

            checkpassword=check_password(password,user.password)
            print(checkpassword)
            if user and checkpassword:
                return user
            return None
        except ScrumyUser.DoesNotExist:
            return None

    def get_user(self,user_id):
        try:
            return ScrumyUser.objects.get(pk=user_id)
        except ScrumyUser.DoesNotExist:
            return None
