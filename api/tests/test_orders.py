from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..schemas.orders import OrderCreate
from types import SimpleNamespace

client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    order_data = {
        "customer_name": "John Doe",
        "description": "Test order"
    }

    order_object = OrderCreate(**order_data)
    fake_customer = SimpleNamespace(id=1)
    db_session.query.return_value.filter.return_value.first.return_value = fake_customer
    created_order = controller.create(db_session, order_object)

    assert created_order is not None
    assert created_order.customer_id == 1
    assert created_order.description == "Test order"
