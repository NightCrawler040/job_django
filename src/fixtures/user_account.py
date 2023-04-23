import pytest

from model_bakery import baker


__all__ = ["user_account", "user_accounts", "user_john"]


@pytest.fixture()
def user_account(db):  # pylint: disable=unused-argument
    def _user(**kwargs):
        return baker.make("accounts.UserAccount", **kwargs)

    return _user


@pytest.fixture()
def user_accounts(db):  # pylint: disable=unused-argument
    return baker.make("accounts.UserAccount", _quantity=99, _bulk_create=True)


@pytest.fixture()
def user_john(db):  # pylint: disable=unused-argument
    return baker.make("accounts.UserAccount", email="john@example.com", first_name="John", last_name="Snake")
