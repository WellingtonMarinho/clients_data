from django.views.generic import ListView
from django.utils import timezone

from clients.models import People


class PeopleView(ListView):
    model = People
    paginate_by = 25
    template_name = 'people_list.html'
    context_object_name = 'persons'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
