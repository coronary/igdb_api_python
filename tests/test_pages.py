import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/pages/single_page.yml', filter_headers=['user-key'])
def test_single_page():
    result = igdb.pages(5)
    assert result != []
    assert result[0]['id'] == 5

@vcr.use_cassette('tests/vcr_cassettes/pages/multiple_page.yml', filter_headers=['user-key'])
def test_multiple_page():
    result = igdb.pages({
        'ids':[50,10,45]
    })
    assert result != []
    assert result[0]['id'] == 50
    assert result[1]['id'] == 10
    assert result[2]['id'] == 45
