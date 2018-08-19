from django.forms import model_to_dict
from django.http import JsonResponse
import json
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Order


# Create your views here.
class OrderView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(OrderView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        order_queryset = Order.objects.prefetch_related()
        order_list = list()

        for o in order_queryset:
            pd = model_to_dict(o)
            pd['order_item'] = list()

            for oi in o.OrderItem.all():
                pd['order_item'].append(model_to_dict(oi))
            order_list.append(pd)

        order_list = json.dumps(order_list)

        return JsonResponse(order_list, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body.decode("UTF-8"))
            Order.objects.create(**data)
            response = {
                'status': 200,
                'type': '+OK',
                'message': 'Successfully Order data recorded',
            }
        except Exception as error:
            response = {
                'status': 500,
                'type': '-ERR',
                'message': 'Internal Server Error',
            }
        return JsonResponse(response, status=response.get('status'))






