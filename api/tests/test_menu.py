import pytest
from fastapi.testclient import TestClient
from ..controllers import menu_items as menuController
from ..main import app
from ..models import menu_items as menuModel

client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_menu_item_success(db_session, mocker):
    menu_data = {
        "item_name": "Cheeseburger",
        "price": 8.99,
        "calories": 500,
        "order_category": "Main"
    }
    menu_object = menuModel.MenuItem(**menu_data)

    created_item = menuController.create(db_session, menu_object)

    assert created_item is not None
    assert created_item.item_name == "Cheeseburger"
    assert created_item.price == 8.99
    assert created_item.calories == 500
    assert created_item.order_category == "Main"


def test_read_all_menu_items(db_session):
    mock_items = [
        menuModel.MenuItem(item_name="Cheeseburger", price=8.99, calories=500, order_category="Main"),
        menuModel.MenuItem(item_name="Fries", price=3.49, calories=300, order_category="Sides")
    ]
    db_session.query.return_value.all.return_value = mock_items

    items = menuController.read_all(db_session)

    assert len(items) == 2
    assert items[0].item_name == "Cheeseburger"
    assert items[1].item_name == "Fries"


def test_read_one_menu_item_success(db_session):
    mock_item = menuModel.MenuItem(item_name="Fries", price=3.49, calories=300, order_category="Sides")
    db_session.query.return_value.filter.return_value.first.return_value = mock_item

    item = menuController.read_one(db_session, 1)

    assert item.item_name == "Fries"
    assert item.price == 3.49
