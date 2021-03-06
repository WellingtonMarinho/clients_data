from django.core.paginator import EmptyPage, Page, PageNotAnInteger, Paginator
from django.utils.functional import cached_property

class DSEPaginator(Paginator):
    """
    Override Django's built-in Paginator class to take in a count/total number of items;
    Elasticsearch provides the total as a part of the query results, so we can minimize hits.
    """
    def __init__(self, *args, **kwargs):
        super(DSEPaginator, self).__init__(*args, **kwargs)
        self._count = self.object_list.hits.total['value']

    @cached_property
    def count(self):
        """Return the total number of objects, across all pages."""
        return self.object_list.hits.total['value']

    def page(self, number):
        # this is overridden to prevent any slicing of the object_list - Elasticsearch has
        # returned the sliced data already.
        number = self.validate_number(number)
        return Page(self.object_list, number, self)