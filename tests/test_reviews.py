import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleReview():
    result = igdb.reviews(7)
    assert result != []
def test_multipleReview():
    result = igdb.reviews({
        'ids':[20,80,34]
    })
    assert result != []
