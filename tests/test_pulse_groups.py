import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/pulse_group/single_pulse_group.yml', filter_headers=['user-key'])
def test_single_pulse_group():
    result = igdb.pulse_groups(5768)
    assert result != []
    assert result[0]['id'] == 5768

@vcr.use_cassette('tests/vcr_cassettes/pulse_group/multiple_pulse_group.yml', filter_headers=['user-key'])
def test_multiple_pulse_group():
    result = igdb.pulse_groups({
        'ids':[5772,5775,5777]
    })
    assert result != []
    assert result[0]['id'] == 5772
    assert result[1]['id'] == 5775
    assert result[2]['id'] == 5777
