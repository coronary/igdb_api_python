import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/game_modes/single_game_mode.yml', filter_headers=['user-key'])
def test_single_game_mode():
    result = igdb.game_modes(1)
    assert result.body != []
    assert result.body[0]['id'] == 1

@vcr.use_cassette('tests/vcr_cassettes/game_modes/multiple_game_mode.yml', filter_headers=['user-key'])
def test_multiple_game_mode():
    result = igdb.game_modes({
        'ids':[2,3,5]
    })
    assert result.body != []
    assert result.body[0]['id'] == 2
    assert result.body[1]['id'] == 3
    assert result.body[2]['id'] == 5
