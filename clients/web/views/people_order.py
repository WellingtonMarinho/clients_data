from django.views.generic import ListView
from django.utils import timezone

from clients.models import People


class PeopleOrderView(ListView):
    model = People
    paginate_by = 10
    template_name = 'people_order_list.html'
    context_object_name = 'people_order'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
