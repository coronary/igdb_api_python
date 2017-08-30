import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/pulse_sources/single_player_perspective.yml', filter_headers=['user-key'])
def test_single_pulse_source():
    result = igdb.pulse_sources(2)
    assert result.body != []
    assert result.body[0]['id'] == 2

@vcr.use_cassette('tests/vcr_cassettes/pulse_sources/multiple_player_perspective.yml', filter_headers=['user-key'])
def test_multiple_pulse_source():
    result = igdb.pulse_sources({
        'ids':[8,9,10]
    })
    assert result.body != []
    assert result.body[0]['id'] == 8
    assert result.body[1]['id'] == 9
    assert result.body[2]['id'] == 10
