import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleCompany():
    result = igdb.companies(2238)
    assert result != []
def test_multipleCompany():
    result = igdb.companies({
        'ids':[2239,2240,2242]
    })
    assert result != []
