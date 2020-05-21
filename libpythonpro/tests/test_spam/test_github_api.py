from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'JessicaLima92', 'id': 55584410,
        'avatar_url': 'https://avatars2.githubusercontent.com/u/55584410?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('JessicaLima92')
    assert 'https://avatars2.githubusercontent.com/u/55584410?v=4' == url
