import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleReview():
    result = igdb.callApi("reviews", 25039)
    assert result.status_code == 200
def test_multipleReview():
    result = igdb.callApi("reviews",{
        'ids':[25044,25042,25041]
    })
    assert result.status_code == 200
