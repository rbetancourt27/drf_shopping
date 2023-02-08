from django.urls import path

from shopping_list.api.views import (
    AddShoppingItemView,
    ListAddShoppingListView,
    ShoppingItemDetailView,
    ShoppingListDetailView,
)

urlpatterns = [
    path(
        "api/shopping-lists/",
        ListAddShoppingListView.as_view(),
        name="all-shopping-lists",
    ),
    path(
        "api/shopping-lists/<uuid:pk>/",
        ShoppingListDetailView.as_view(),
        name="shopping-list-detail",
    ),
    path(
        "api/shopping-lists/<uuid:pk>/shopping-items/",
        AddShoppingItemView.as_view(),
        name="add-shopping-item",
    ),
    path(
        "api/shopping-lists/<uuid:pk>/shopping-items/<uuid:item_pk>/",
        ShoppingItemDetailView.as_view(),
        name="shopping-item-detail",
    ),
]
