import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/pulses/single_pulse.yml', filter_headers=['user-key'])
def test_single_pulse():
    result = igdb.pulses(24000)
    assert result != []
    assert result[0]['id'] == 24000

@vcr.use_cassette('tests/vcr_cassettes/pulses/multiple_pulses.yml', filter_headers=['user-key'])
def test_multiple_pulses():
    result = igdb.pulses({
        'ids':[25040,25047,25000]
    })
    assert result != []
    assert result[0]['id'] == 25040
    assert result[1]['id'] == 25047
    assert result[2]['id'] == 25000
