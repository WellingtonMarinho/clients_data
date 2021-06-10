from elasticsearch_dsl import analyzer, token_filter


synonym_tokenfilter = token_filter(
    'synonym_tokenfilter',
    'synonym',
    synonyms=[
        'reactjs, react', # <- ADD more in future
        'futebol, fut',
    ]
)

brazilian_stop_filter = token_filter(
    'brazilian_stop_filter',
    'stop',
    stopwords='_brazilian_'
)

brazilian_stemmer_filter = token_filter(
    'brazilian_stemmer_filter',
    'stemmer', # < - analiza radicais.
    language='brazilian'
)

text_analyzer = analyzer(
    'text_analyzer',
    tokenize='standard',
    filter=[
        'lowercase', # <-  indexa tudo em minúsculo
        'asciifolding',
        synonym_tokenfilter
    ],
    char_filter=['html_strip']
)

brazilian_text_analyzer = analyzer(
    'text_analyzer',
    tokenize='standard',
    filter=[
        'lowercase',
        'asciifolding',
        brazilian_stop_filter,
        synonym_tokenfilter,
        brazilian_stemmer_filter
    ],
    char_filter=['html_strip']
)
