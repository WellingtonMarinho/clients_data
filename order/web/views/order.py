from django.views.generic import ListView
from django.utils import timezone

from order.models import Order


class OrderView(ListView):
    model = Order
    paginate_by = 25
    template_name = 'order_list.html'
    context_object_name = 'orders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
