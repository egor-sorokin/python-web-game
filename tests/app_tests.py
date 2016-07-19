from nose.tools import *
from bin.app import app
from tests.tools import assert_response


def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status='200')

    # test our first GET request to /gothon
    resp = app.request("/gothon_game")
    assert_response(resp, status='200')

    # test our first GET request to /zombie
    resp = app.request("/zombie_game")
    assert_response(resp, status='200')
