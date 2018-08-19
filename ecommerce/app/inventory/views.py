from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product
import json
import logging

slack_logger = logging.getLogger('django.request')


class ProductView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        product_queryset = Product.objects.values()
        product_list = list()

        for p in product_queryset:
            product_list.append(p)

        return JsonResponse(product_list, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body.decode("UTF-8"))
            Product.objects.create(**data)
            response = {
                'status': 200,
                'type': '+OK',
                'message': 'Successfully Product data recorded',
            }
        except Exception as error:
            slack_logger.error("Error while Product Create", exc_info=True)
            response = {
                'status': 500,
                'type': '-ERR',
                'message': 'Internal Server Error',
            }
        return JsonResponse(response, status=response.get('status'))


class ProductUpdateView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)

    def put(self, request, pk):
        try:
            data = json.loads(request.body.decode("UTF-8"))
            Product.objects.filter(id=pk).update(**data)
            response = {
                'status': 200,
                'type': '+OK',
                'message': 'Successfully Product data updated',
            }
        except Exception as error:
            slack_logger.error("Error while Product Update", exc_info=True)
            response = {
                'status': 500,
                'type': '-ERR',
                'message': 'Internal Server Error',
            }
        return JsonResponse(response, status=response.get('status'))

    def delete(self, request, pk):
        try:
            product_delete = Product.objects.filter(id=pk).delete()
            if product_delete:
                response = {
                            'status': 200,
                            'type': '+OK',
                            'message': 'Successfully Product data Deleted',
                }
            else:
                response = {
                    'status': 200,
                    'type': '+OK',
                    'message': 'Data not available in database',
                }
        except Exception as error:
            slack_logger.error("Error while Product Delete", exc_info=True)
            response = {
                        'status': 500,
                        'type': '-ERR',
                        'message': 'Internal Server Error',
            }
        return JsonResponse(response, status=response.get('status'))






