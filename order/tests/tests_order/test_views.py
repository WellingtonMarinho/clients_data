from django.test import TestCase


class OrderPostAPIViewTestCase(TestCase):
    def setUp(self):
        body = {
            "client": 13,
            "items": [
                {
                    "product": 2,
                    "quantity": 12
            },
            {
                "product": 5,
                "quantity": 2
            },
            {
                "product": 12,
                "quantity": 6
            },
            {
                "product": 1,
                "quantity": 2
            }
             ]
        }
