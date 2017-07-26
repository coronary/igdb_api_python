import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleFranchises():
    result = igdb.callApi("franchises", 25039)
    assert result.status_code == 200
def test_multipleFranchises():
    result = igdb.callApi("franchises",{
        'ids':[25044,25042,25041]
    })
    assert result.status_code == 200
