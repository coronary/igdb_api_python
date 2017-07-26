import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleFeed():
    result = igdb.feeds(129989)
    assert result != []
def test_singleFeed():
    result = igdb.feeds({
        'ids':[129993,129992,129985]
    })
    assert result != []
