import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/pulses/single_pulse.yml', filter_headers=['user-key'])
def test_single_pulse():
    result = igdb.pulses(24000)
    assert result.body != []
    assert result.body[0]['id'] == 24000

@vcr.use_cassette('tests/vcr_cassettes/pulses/multiple_pulses.yml', filter_headers=['user-key'])
def test_multiple_pulses():
    result = igdb.pulses({
        'ids':[25040,25047,25000]
    })
    assert result.body != []
    assert result.body[0]['id'] == 25040
    assert result.body[1]['id'] == 25047
    assert result.body[2]['id'] == 25000

@vcr.use_cassette('tests/vcr_cassettes/pulses/limit.yml', filter_headers=['user-key'])
def test_limit():
    result = igdb.pulses({
        'fields':'title',
        'limit':3,
    })
    assert result.body != []
    assert len(result.body) == 3
    assert result.body[0]['id'] == 25039

@vcr.use_cassette('tests/vcr_cassettes/pulses/offset.yml', filter_headers=['user-key'])
def test_offset():
    result = igdb.pulses({
        'fields':'title',
        'offset':3,
    })
    assert result.body != []
    assert result.body[0]['id'] == 25042
