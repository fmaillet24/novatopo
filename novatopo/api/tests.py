import graphene
from django.test.testcases import TestCase
from novatopo.schema import Query

from api.models import Activity, Business


def initialize():
    obj = Activity(name='Karting')
    obj.save()

    objj = Activity(name='Acrobranche')
    objj.save()

    bus = Business(name='Le Mans Ask', address="Chemin aux Boeufs")
    bus.save()

    buss = Business(name='Acrobranche Air', address="Chemin aux Boeufs")
    buss.save()


class ApiTestCase(TestCase):

    def setUp(self):
        super().setUp()
        initialize()

    def test_all_activity(self):
        query = """
            query {
              allActivity {
                id
                name
              }
            }
        """
        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        assert not result.errors
        assert result.data == {"allActivity": [
            {
                "id": "1",
                "name": "Karting"
            },
            {
                "id": "2",
                "name": "Acrobranche"
            },
        ]}

    def test_all_business(self):
        query = """
            query {
              allBusiness {
                id
                name
                address
              }
            }
        """
        schema = graphene.Schema(query=Query)
        result = schema.execute(query)
        assert not result.errors
        assert result.data == {"allBusiness": [
            {
                "id": "3",
                "name": "Le Mans Ask",
                "address": "Chemin aux Boeufs"
            },
            {
                "id": "4",
                "name": "Acrobranche Air",
                "address": "Chemin aux Boeufs"
            },
        ]}
