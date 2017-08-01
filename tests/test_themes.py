import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/themes/single_theme.yml', filter_headers=['user-key'])
def test_single_theme():
    result = igdb.themes(34)
    assert result != []

@vcr.use_cassette('tests/vcr_cassettes/themes/multiple_theme.yml', filter_headers=['user-key'])
def test_multiple_theme():
    result = igdb.themes({
        'ids':[22,23,28]
    })
    assert result != []
