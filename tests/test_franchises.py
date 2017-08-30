import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/franchises/single_franchises.yml', filter_headers=['user-key'])
def test_single_franchises():
    result = igdb.franchises(1040)
    assert result.body != []

@vcr.use_cassette('tests/vcr_cassettes/franchises/multiple_franchises.yml', filter_headers=['user-key'])
def test_multiple_franchises():
    result = igdb.franchises({
        'ids':[1043,1,2]
    })
    assert result.body != []
    assert result.body[0]['id'] == 1043
    assert result.body[1]['id'] == 1
    assert result.body[2]['id'] == 2
