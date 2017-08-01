import pytest, os, vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/collections/multiple_character.yml', filter_headers=['user-key'])
def test_single_collection():
    result = igdb.collections(1194)
    assert result != []
    assert result[0]['id'] == 1194

@vcr.use_cassette('tests/vcr_cassettes/collections/multiple_collection.yml', filter_headers=['user-key'])
def test_multiple_collection():
    result = igdb.collections({
        'ids':[1198,1199,1200]
    })
    assert result != []
    assert result[0]['id'] == 1198
    assert result[1]['id'] == 1199
    assert result[2]['id'] == 1200
