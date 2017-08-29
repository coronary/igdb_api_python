import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/platforms/single_platform.yml', filter_headers=['user-key'])
def test_single_platform():
    result = igdb.platforms(11)
    assert result != []
    assert result[0]['id'] == 11

@vcr.use_cassette('tests/vcr_cassettes/platforms/multiple_platform.yml', filter_headers=['user-key'])
def test_multiple_platform():
    result = igdb.platforms({
        'ids':[13,5,3]
    })
    assert result != []
    assert result[0]['id'] == 13
    assert result[1]['id'] == 5
    assert result[2]['id'] == 3

@vcr.use_cassette('tests/vcr_cassettes/platforms/search.yml')
def test_game_search_multi_and_single():
    result = igdb.platforms({
        'search': "xbox one",
        'fields' : 'name'
    })
    print(result)
    assert result != []
    assert result[0]['id'] == 49
    assert type(result[0]) == dict
