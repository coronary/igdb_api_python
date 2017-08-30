import pytest, os, vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/feeds/single_feed.yml', filter_headers=['user-key'])
def test_single_feed():
    result = igdb.feeds(129989)
    assert result.body != []
    assert result.body[0]['id'] == 129989

@vcr.use_cassette('tests/vcr_cassettes/feeds/multiple_feed.yml', filter_headers=['user-key'])
def test_multiple_feed():
    result = igdb.feeds({
        'ids':[129993,129992,129985]
    })
    assert result != []
    assert result.body[0]['id'] == 129993
    assert result.body[1]['id'] == 129992
    assert result.body[2]['id'] == 129985
