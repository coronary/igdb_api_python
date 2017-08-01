import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/player_perspectives/single_player_perspective.yml', filter_headers=['user-key'])
def test_single_player_perspective():
    result = igdb.player_perspectives(2)
    assert result != []
    assert result[0]['id'] == 2

@vcr.use_cassette('tests/vcr_cassettes/player_perspectives/multiple_player_perspective.yml', filter_headers=['user-key'])
def test_multiple_player_perspective():
    result = igdb.player_perspectives({
        'ids':[7,5,4]
    })
    assert result != []
    assert result[0]['id'] == 7
    assert result[1]['id'] == 5
    assert result[2]['id'] == 4
