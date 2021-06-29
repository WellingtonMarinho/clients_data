from decouple import config


ES_CONNECTIONS = {
    config('ELASTICSEARCH_CONNECTION_ALIAS', 'default'): {
        'hosts': [config('ELASTICSEARCH_HOST')],
    }
}

PROJECT_INDEX_PEOPLE = config('PROJECT_INDEX_PEOPLE', 'index.peoples')

ES_INDEXES = {
    config('ELASTICSEARCH_CONNECTION_ALIAS', 'default'): [
        (PROJECT_INDEX_PEOPLE, 'clients.document.PeopleDocument')
    ]
}

ES_DEFAULT_BATCH_SIZE = config('ES_DEFAULT_BATCH_SIZE', default=100, cast=int)
