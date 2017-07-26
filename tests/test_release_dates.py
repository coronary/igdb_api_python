import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleReleaseDate():
    result = igdb.release_dates(86653)
    assert result != []
def test_multipleReleaseDate():
    result = igdb.release_dates({
        'ids':[86660,86663,15683]
    })
    assert result != []
