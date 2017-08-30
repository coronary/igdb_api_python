import pytest, os, vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/characters/single_character.yml', filter_headers=['user-key'])
def test_single_character():
    result = igdb.characters(8529)
    assert result.body != []
    assert result.body[0]['id'] == 8529

@vcr.use_cassette('tests/vcr_cassettes/characters/multiple_character.yml', filter_headers=['user-key'])
def test_multiple_character():
    result = igdb.characters({
        'ids':[8530,8531,8533]
    })
    assert result.body != []
    assert result.body[0]['id'] == 8530
    assert result.body[1]['id'] == 8531
    assert result.body[2]['id'] == 8533

@vcr.use_cassette('tests/vcr_cassettes/characters/search.yml')
def test_game_search_multi_and_single():
    result = igdb.characters({
        'search': "geralt of rivia",
        'fields' : 'name'
    })
    print(result)
    assert result.body != []
    assert result.body[0]['id'] == 1453
    assert type(result.body[0]) == dict
