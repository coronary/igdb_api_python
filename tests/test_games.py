import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/games/single_game.yml', filter_headers=['user-key'])
def test_single_game():
    result = igdb.games(1942)
    assert result != []
    assert result[0]['id'] == 1942

@vcr.use_cassette('tests/vcr_cassettes/games/multiple_games.yml', filter_headers=['user-key'])
def test_multiple_games():
    result = igdb.games({
        'ids':[27193,23212,1942]
    })
    assert result != []
    assert result[0]['id'] == 27193
    assert result[1]['id'] == 23212
    assert result[2]['id'] == 1942
