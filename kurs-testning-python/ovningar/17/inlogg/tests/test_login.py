import pytest
from pytest_bdd import scenario, given, when, then, parsers
from src.auth import AuthService


@pytest.fixture
def auth_service():
    return AuthService()


@pytest.fixture
def login_result():
    return {}


@scenario("../features/login.feature", "Lyckad inloggning")
def test_lyckad_inloggning():
    pass


@scenario("../features/login.feature", "Felaktigt lösenord")
def test_felaktigt_losenord():
    pass


@scenario("../features/login.feature", "Icke-existerande användare")
def test_okand_anvandare():
    pass


@given(
    parsers.parse('att användaren "{username}" finns med lösenord "{password}"'),
    target_fixture="registered_user",
)
def register_user(auth_service, username, password):
    auth_service.register(username, password)
    return username


@when(
    parsers.parse('användaren loggar in med "{username}" och "{password}"'),
    target_fixture="login_result",
)
def do_login(auth_service, username, password):
    return auth_service.login(username, password)


@then("ska inloggningen lyckas")
def check_success(login_result):
    assert login_result["success"] is True


@then("ska inloggningen misslyckas")
def check_failure(login_result):
    assert login_result["success"] is False


@then(parsers.parse('felmeddelandet ska vara "{message}"'))
def check_error_message(login_result, message):
    assert login_result["error"] == message
