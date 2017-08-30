import pytest, os, vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/game_engines/single_game_engine.yml', filter_headers=['user-key'])
def test_single_game_engine():
    result = igdb.game_engines(67)
    assert result.body != []
    assert result.body[0]['id'] == 67

@vcr.use_cassette('tests/vcr_cassettes/game_engines/multiple_game_engine.yml', filter_headers=['user-key'])
def test_multiple_game_engine():
    result = igdb.game_engines({
        'ids':[367,363,359]
    })
    assert result.body != []
    assert result.body[0]['id'] == 367
    assert result.body[1]['id'] == 363
    assert result.body[2]['id'] == 359
