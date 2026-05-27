import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_numbers2(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize('os', ['mac', 'linux', 'windows', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'firefox', 'webkit'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0



@pytest.fixture(params=['chromium', 'firefox', 'webkit'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on: {browser}')


@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_user_with_operation(self, user: str, account: str):
        print(f'User with operation: {user}')

    def test_user_without_operation(self, user: str):
        print(f'User with no operation: {user}')


users = {
    '+70000000000000':'User with money on bank account',
    '+70000000000011':'User with no money on bank account',
    '+70000000000022':'User with operation on bank account'
}


@pytest.mark.parametrize('phone_number',
                         users.keys(),
                         ids=lambda phone_number: f'{phone_number} : {users[phone_number]}'
                         )
def test_identifiers(phone_number: str):
    ...