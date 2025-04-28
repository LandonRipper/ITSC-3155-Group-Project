import pytest
from fastapi.testclient import TestClient
from ..controllers import customers as customerController
from ..main import app
from ..models import customer as customerModel

client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_customer_success(db_session):
    customer_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    customer_object = customerModel.Customer(**customer_data)

    created_customer = customerController.create(db_session, customer_object)

    assert created_customer is not None
    assert created_customer.name == "John Doe"
    assert created_customer.email == "john.doe@example.com"


def test_read_all_customers(db_session):
    mock_customers = [
        customerModel.Customer(name="John Doe", email="john@example.com"),
        customerModel.Customer(name="Jane Smith", email="jane@example.com")
    ]
    db_session.query.return_value.all.return_value = mock_customers

    customers = customerController.read_all(db_session)

    assert len(customers) == 2
    assert customers[0].name == "John Doe"
    assert customers[1].name == "Jane Smith"


def test_read_one_customer_success(db_session):
    mock_customer = customerModel.Customer(name="John Doe", email="john@example.com")
    db_session.query.return_value.filter.return_value.first.return_value = mock_customer

    customer = customerController.read_one(db_session, 1)

    assert customer.name == "John Doe"
    assert customer.email == "john@example.com"
