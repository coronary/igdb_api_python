import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/keywords/single_keyword.yml', filter_headers=['user-key'])
def test_single_keyword():
    result = igdb.keywords(1083)
    assert result != []
    assert result[0]['id'] == 1083

@vcr.use_cassette('tests/vcr_cassettes/keywords/multiple_keyword.yml', filter_headers=['user-key'])
def test_multiple_keyword():
    result = igdb.keywords({
        'ids':[1086,1090,193]
    })
    assert result != []
    assert result[0]['id'] == 1086
    assert result[1]['id'] == 1090
    assert result[2]['id'] == 193
