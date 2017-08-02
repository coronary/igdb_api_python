import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/release_dates/single_release_date.yml', filter_headers=['user-key'])
def test_single_release_date():
    result = igdb.release_dates(86653)
    assert result != []
    assert result[0]['id'] == 86653

@vcr.use_cassette('tests/vcr_cassettes/release_dates/multiple_release_date.yml', filter_headers=['user-key'])
def test_multiple_release_date():
    result = igdb.release_dates({
        'ids':[86660,86663,15683]
    })
    assert result != []
    assert result[0]['id'] == 86660
    assert result[1]['id'] == 86663
    assert result[2]['id'] == 15683

@vcr.use_cassette('tests/vcr_cassettes/release_dates/filters.yml', filter_headers=['user-key'])
def test_multiple_release_date():
    result = igdb.release_dates({
        'filters' :{
            "[platform][eq]": 48,
            "[date][gt]"    : 1501586921000
        },
        'fields':"game",
        'order': 'date:asc'
    })
    assert result != []
    assert result[0]['game'] == 11797

@vcr.use_cassette('tests/vcr_cassettes/release_dates/single_expander.yml', filter_headers=['user-key'])
def test_single_expander():
    result = igdb.release_dates({
        'ids' : 86653,
        'expand':"game",
    })
    assert result != []
    assert result[0]['game']['id'] == 38722
@vcr.use_cassette('tests/vcr_cassettes/release_dates/multiple_expander.yml', filter_headers=['user-key'])
def test_multiple_expander():
    result = igdb.release_dates({
        'ids' : 86653,
        'expand' : ['game','platform']
    })
    assert result != []
    assert result[0]['game']['id'] == 38722
    assert result[0]['platform']['id'] == 34
