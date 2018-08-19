import json
from django.forms import model_to_dict
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, OrderItem


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
            for py in o.order_for_order_item.all():
                pd['order_item'].append(model_to_dict(py))
            order_list.append(pd)

        return JsonResponse(order_list, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body.decode("UTF-8"))
            order_item = data.pop('order_item')

            order_id = Order.objects.create(**data)

            order_item_obj = [
                OrderItem(
                    order=order_id,
                    product_id=item.get('product'),
                    quantity=item.get('quantity')
                )
                for item in order_item
            ]
            OrderItem.objects.bulk_create(order_item_obj)

            response = {
                'status': 200,
                'type': '+OK',
                'message': 'Successfully Order Created',
                'order_id': order_id.id
            }
        except Exception as error:
            response = {
                'status': 500,
                'type': '-ERR',
                'message': 'Internal Server Error',
            }
        return JsonResponse(response, status=response.get('status'))