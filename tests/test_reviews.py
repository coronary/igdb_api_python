import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/reviews/single_review.yml', filter_headers=['user-key'])
def test_single_review():
    result = igdb.reviews(7)
    assert result != []
    assert result[0]['id'] == 7

@vcr.use_cassette('tests/vcr_cassettes/reviews/multiple_review.yml', filter_headers=['user-key'])
def test_multiple_review():
    result = igdb.reviews({
        'ids':[20,80,34]
    })
    assert result != []
    assert result[0]['id'] == 20
    assert result[1]['id'] == 80
    assert result[2]['id'] == 34
