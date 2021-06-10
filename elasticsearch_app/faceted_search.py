from elasticsearch_dsl import FacetedSearch, Search
from elasticsearch_dsl.faceted_search import FacetedResponse


class FacetedSearchMixin(FacetedSearch):

    def __init__(self, query=None, filters={}, sort=(), params=None, **kwargs):
        self._params = params
        super().__init__(query, filters, sort)

    def search(self):
        s = Search(doc_type=self.doc_types, index=self.index, using=self.using)
        if self._params:
            s = s.params(**self._params)
        return s.response_class(FacetedResponse)
