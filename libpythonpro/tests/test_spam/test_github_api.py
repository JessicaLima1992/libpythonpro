from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars2.githubusercontent.com/u/55584410?v=4'
    resp_mock.json.return_value = {
        'login': 'JessicaLima92', 'id': 55584410,
        'avatar_url': url,
    }
    get_mocker = mocker.patch('libpythonpro.github_api.requests.get')
    get_mocker.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('JessicaLima92')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('JessicaLima1992')
    assert 'https://avatars3.githubusercontent.com/u/63428577?v=4' == url
