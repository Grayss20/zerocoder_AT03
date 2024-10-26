import pytest
from hw import get_cat_image


def test_get_cat_image(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'url': 'https://example.com/cat.jpg'}
    image = get_cat_image()
    assert image == {'url': 'https://example.com/cat.jpg'}


def test_get_cat_image_error(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 404
    image = get_cat_image()
    assert image is None
