import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleCollection():
    result = igdb.callApi("collections", 25039)
    assert result.status_code == 200
def test_multipleCollection():
    result = igdb.callApi("collections",{
        'ids':[25044,25042,25041]
    })
    assert result.status_code == 200
