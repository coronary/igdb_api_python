import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singlePage():
    result = igdb.pages(5)
    assert result != []
def test_multiplePage():
    result = igdb.pages({
        'ids':[50,10,45]
    })
    assert result != []
