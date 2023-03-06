import pytest
from rest_framework.test import APIClient

from shopping_list.models import ShoppingItem, ShoppingList


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture()
def shopping_list():
    def _shopping_list(name):
        shopping_list = ShoppingList.objects.create(name=name)
        return shopping_list

    return _shopping_list


@pytest.fixture()
def shopping_item(shopping_list):
    def _shopping_item(name):
        shopping_item = ShoppingItem.objects.create(
            name=name, purchased=False, shopping_list=shopping_list(name)
        )

        return shopping_item

    return _shopping_item
