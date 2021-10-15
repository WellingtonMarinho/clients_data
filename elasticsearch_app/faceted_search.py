from elasticsearch_dsl import FacetedSearch, Search
from elasticsearch_dsl.faceted_search import FacetedResponse


class FacetedSearchMixin(FacetedSearch):

    def __init__(self, query=None, filters=None, sort=(), params=None, **kwargs):
        if filters is None:
            filters = {}
        self._params = params
        super().__init__(query, filters, sort)

    def search(self):
        """
        Returns the base Search object to which the facets are added.

        You can customize the query by overriding this method and returning a
        modified search object.
        """
        s = Search(doc_type=self.doc_types, index=self.index, using=self.using)
        if self._params:
            s = s.params(**self._params)
        return s.response_class(FacetedResponse)


class CreateAndModifiedFacetedSearch(FacetedSearch):

    def __init__(
            self,
            query=None,
            filters=None,
            sort=(),
            created_at=None,
            modified_at=None,
            params=None,
            **kwargs
         ):
        if filters is None:
            filters = {}
        self._created_at = created_at
        self._modified_at = modified_at
        self._params = params

        super().__init__(query, filters, sort)

    def search(self):
        s = super().search()

        if self._params:
            s = s.params(**self._params)

        if self._created_at:
            s = s.filter('range', created_at={'gte': self._created_at})

        if self._modified_at:
            s = s.filter('range', modified_at={'gte': self._modified_at})

        return s
