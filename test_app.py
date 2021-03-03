import pytest

from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_comments_returns_expected_format(client, mocker):
    mocker.patch('main.comment.list', return_value=[])
    res = client.get("/comments")
    assert res.status_code == 200
    assert 'comments' in res.json
    assert len(res.json['comments']) == 0
