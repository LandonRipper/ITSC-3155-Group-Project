import pytest
from types import SimpleNamespace
from ..controllers import payments as controller
from ..schemas.payments import PaymentCreate, PaymentUpdate
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_payment_success(db_session):
    payment_data = {
        "order_id": 1,
        "order_detail_id": 10,
        "card_info": "4111-1111-1111-1111",
        "transaction_status": "Completed",
        "payment_type": "Credit"
    }
    request = PaymentCreate(**payment_data)

    db_session.query.return_value.filter.return_value.first.side_effect = [
        SimpleNamespace(id=10, price=29.99)
    ]

    result = controller.create(db_session, request)
    assert result is not None
    assert result.payment_amount == 29.99
    assert result.order_id == 1
    assert result.transaction_status == "Completed"


def test_read_one_payment_found(db_session):
    fake_payment = SimpleNamespace(id=1, order_id=1, card_info="1234", transaction_status="Success", payment_type="Debit")
    db_session.query.return_value.filter.return_value.first.return_value = fake_payment
    result = controller.read_one(db_session, 1)
    assert result.id == 1
    assert result.transaction_status == "Success"


def test_read_one_payment_not_found(db_session):
    db_session.query.return_value.filter.return_value.first.return_value = None
    with pytest.raises(Exception) as e:
        controller.read_one(db_session, 999)
    assert "Payment ID not found" in str(e.value)


def test_update_payment_success(db_session):
    existing_payment = SimpleNamespace(id=1, card_info="old", transaction_status="old", payment_type="old")
    db_session.query.return_value.filter.return_value.first.return_value = existing_payment
    db_session.query.return_value.filter.return_value.first.return_value.dict = lambda: {
        "card_info": "old", "transaction_status": "old", "payment_type": "old"
    }
    update_data = PaymentUpdate(card_info="new_card", transaction_status="Completed", payment_type="Credit")
    db_session.query.return_value.filter.return_value.first.return_value.dict = lambda: update_data.dict()
    updated = controller.update(db_session, 1, update_data)
    assert updated is not None


def test_delete_payment_success(db_session):
    db_session.query.return_value.filter.return_value.first.return_value = True
    response = controller.delete(db_session, 1)
    assert response.status_code == 204


def test_delete_payment_not_found(db_session):
    db_session.query.return_value.filter.return_value.first.return_value = None
    with pytest.raises(Exception) as e:
        controller.delete(db_session, 999)
    assert "Payment ID not found" in str(e.value)
