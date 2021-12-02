from .django import  *

SHELL_PLUS_PRE_IMPORTS = (
    ('re'),
    ('clients.tests.factories', ('PeopleGenerator',)),
    ('order.tests.factories', ('ProductsGenerator', 'OrderGenerator')),
)

SHELL_PLUS = "ipython"