import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/games/single_game.yml', filter_headers=['user-key'])
def test_single_game():
    result = igdb.games(1942)
    assert result.body != []
    assert result.body[0]['id'] == 1942

@vcr.use_cassette('tests/vcr_cassettes/games/multiple_games.yml', filter_headers=['user-key'])
def test_multiple_games():
    result = igdb.games({
        'ids':[27193,23212,1942]
    })
    assert result.body != []
    assert result.body[0]['id'] == 27193
    assert result.body[1]['id'] == 23212
    assert result.body[2]['id'] == 1942

@vcr.use_cassette('tests/vcr_cassettes/games/order.yml', filter_headers=['user-key'])
def test_order():
    result = igdb.games({
        'fields': 'name',
        'order': 'popularity:desc'
    })
    assert result.body != []
    assert result.body[0]['id'] == 25657

@vcr.use_cassette('tests/vcr_cassettes/games/single_field.yml', filter_headers=['user-key'])
def test_single_field():
    result = igdb.platforms({
        'ids':42,
        'fields' : 'games'
    })
    assert result.body != []
    assert len(result.body[0]) == 2

@vcr.use_cassette('tests/vcr_cassettes/games/multiple_field.yml', filter_headers=['user-key'])
def test_multiple_field():
    result = igdb.platforms({
        'ids':42,
        'fields' : ['games','name']
    })
    assert result.body != []
    assert len(result.body[0]) == 3

@vcr.use_cassette('tests/vcr_cassettes/games/search.yml')
def test_game_search_multi_and_single():
    result = igdb.games({
        'search': "battlefield 1",
        'fields' : 'name'
    })
    print(result.body)
    assert result.body != []
    assert result.body[0]['id'] == 18320
    assert type(result.body[0]) == dict

@vcr.use_cassette('tests/vcr_cassettes/games/scroll.yml')
def test_game_scroll():
    result = igdb.games({
        'fields' : 'name',
        'scroll' : 1,
        'limit' : 50
    })
    print(result)
    assert result.body != []
    assert result.body[0]['id'] == 19326

    response = igdb.scroll(result)
    assert response.body != []
    assert response.body[0]['id'] == 48854
    response = igdb.scroll(result)
    assert response.body != []
    assert response.body[0]['id'] == 49126
