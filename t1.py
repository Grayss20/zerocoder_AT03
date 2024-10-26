import pytest
from m1 import get_github_user


def test_get_github_user(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'grayss20',
        'id': 1
    }
    username = 'grayss20'
    user = get_github_user(username)
    assert user == {'login': 'grayss20', 'id': 1}


def test_get_github_user_error(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 404
    username = 'grayss20'
    user = get_github_user(username)
    assert user is None
