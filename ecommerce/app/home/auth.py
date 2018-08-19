import json
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.db import IntegrityError
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from ecommerce.app.user_profile.helper import create_user
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout


class SignUp(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SignUp, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            data = json.loads(request.body.decode("UTF-8"))
            user = create_user(request, **data)
            login(request, user)
            response = {
                'status': 200,
                'type': '+OK',
                'url': settings.DASHBOARD_URL,
                'message': 'Successfully Signed Up',
            }
        except IntegrityError as e:
            response = {
                'status': 501,
                'type': '-ERR',
                'message': 'Email already exist',
            }
        except Exception as error:
            response = {
                'status': 500,
                'type': '-ERR',
                'message': 'Internal Server Error',
            }
        return JsonResponse(response, status=response.get('status'))


class Login(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Login, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            data = json.loads(request.body.decode("UTF-8"))
            email = data.get('email', None)
            password = data.get('password', None)
            user = authenticate(username=email, password=password)

            if user is not None:
                login(request, user)
                response = {
                    'status': 200,
                    'type': '+OK',
                    'url': settings.DASHBOARD_URL,
                    'message': 'Login Successfully',
                }
            else:
                response = {
                    'status': 501,
                    'type': '-ERR',
                    'message': 'Email or Password wrong',
                }

        except Exception as error:
            response = {
                'status': 500,
                'type': '-ERR',
                'message': 'Internal Server Error',
            }
        return JsonResponse(response, status=response.get('status'))


class Logout(View):

    def get(self, request):
       logout(request)
       return redirect('/login/')
