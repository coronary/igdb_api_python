import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/companies/single_company.yml', filter_headers=['user-key'])
def test_single_company():
    result = igdb.companies(2238)
    assert result.body != []
    assert result.body[0]['id'] == 2238

@vcr.use_cassette('tests/vcr_cassettes/companies/multiple_company.yml', filter_headers=['user-key'])
def test_multiple_company():
    result = igdb.companies({
        'ids':[2239,2240,2242]
    })
    assert result.body != []
    assert result.body[0]['id'] == 2239
    assert result.body[1]['id'] == 2240
    assert result.body[2]['id'] == 2242

@vcr.use_cassette('tests/vcr_cassettes/companies/search.yml')
def test_game_search_multi_and_single():
    result = igdb.companies({
        'search': "ea",
        'fields' : 'name'
    })
    print(result)
    assert result.body != []
    assert result.body[0]['id'] == 277
    assert type(result.body[0]) == dict
