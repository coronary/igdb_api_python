import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/people/single_people.yml', filter_headers=['user-key'])
def test_single_people():
    result = igdb.people(50)
    assert result.body != []
    assert result.body[0]['id'] == 50

@vcr.use_cassette('tests/vcr_cassettes/people/multiple_people.yml', filter_headers=['user-key'])
def test_multiple_people():
    result = igdb.people({
        'ids':[69159,69153,25041]
    })
    assert result.body != []
    assert result.body[0]['id'] == 69159
    assert result.body[1]['id'] == 69153
    assert result.body[2]['id'] == 25041

@vcr.use_cassette('tests/vcr_cassettes/people/search.yml')
def test_game_search_multi_and_single():
    result = igdb.people({
        'search' : "gabe newell",
        'fields' : 'name'
    })
    print(result.body)
    assert result.body != []
    assert result.body[0]['id'] == 108558
    assert type(result.body[0]) == dict

@vcr.use_cassette('tests/vcr_cassettes/people/scroll.yml')
def test_game_scroll():
    result = igdb.people({
        'fields' : 'name',
        'scroll' : 1,
        'limit' : 50
    })
    print(result)
    assert result.body != []
    assert result.body[0]['id'] == 18648

    response = igdb.scroll(result)
    assert response.body != []
    assert response.body[0]['id'] == 18903
    response = igdb.scroll(result)
    assert response.body != []
    assert response.body[0]['id'] == 19211
