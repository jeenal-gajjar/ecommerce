from django.contrib.auth import get_user_model


def create_user(request, **data):
   """

   Create new user for default django.contrib.auth
   key pair value data required:
   first_name, last_name, username, email, password

   :param request:
   :param key value pair data:
   :return: user object:
   """
   user_model = get_user_model()
   user = user_model.objects.create_user(
       **data,
   )
   return user

