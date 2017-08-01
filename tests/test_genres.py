import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/genres/single_genre.yml', filter_headers=['user-key'])
def test_single_genre():
    result = igdb.genres(2)
    assert result != []
    assert result[0]['id'] == 2

@vcr.use_cassette('tests/vcr_cassettes/genres/multiple_genre.yml', filter_headers=['user-key'])
def test_multiple_genre():
    result = igdb.genres({
        'ids':[7,5,10]
    })
    assert result != []
    assert result[0]['id'] == 7
    assert result[1]['id'] == 5
    assert result[2]['id'] == 10
