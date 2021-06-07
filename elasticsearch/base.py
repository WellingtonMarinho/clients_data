# Based on: https://medium.com/@harshvb7/managing-elasticsearch-in-django-like-a-pro-adfcd984920d

import elasticsearch_dsl as es
from django.conf import settings


class Documentbase(es.Document):

    @classmethod
    def get_index_queryset(cls):
        """
        Base queryset for indexing the document.
        """
        return cls.get_model().objects.all()

    @classmethod
    def get_index_config(cls):
        """
        Returns the index config on which current actions are performed.
        {
            'connection_name': 'default',
            'connection': {'hosts': http://localhost:9200},
            'index_name': 'blog',
            'index_class': 'some_app.indexes.Article',
        }
        """
        connections = settings.ES_CONNECTION
        indexes = settings.ES_INDEXES
        index_name = cls._index_name
        print(connections)
        print()
        print()
        print()
        print()
        print()
        print(dir(connections))