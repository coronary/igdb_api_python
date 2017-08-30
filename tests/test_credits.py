import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/credits/single_credit.yml', filter_headers=['user-key'])
def test_single_credit():
    result = igdb.credits(1073917668)
    assert result.body != []

@vcr.use_cassette('tests/vcr_cassettes/credits/multiple_credit.yml', filter_headers=['user-key'])
def test_multiple_credit():
    result = igdb.credits({
        'ids':[1073917668,1073917629,1073917617]
    })
    assert result != []
    assert result.body[0]['id'] == 1073917668
    assert result.body[1]['id'] == 1073917629
    assert result.body[2]['id'] == 1073917617
