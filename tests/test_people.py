import pytest, os,vcr

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

@vcr.use_cassette('tests/vcr_cassettes/people/single_people.yml', filter_headers=['user-key'])
def test_single_people():
    result = igdb.people(50)
    assert result != []
    assert result[0]['id'] == 50

@vcr.use_cassette('tests/vcr_cassettes/people/multiple_people.yml', filter_headers=['user-key'])
def test_multiple_people():
    result = igdb.people({
        'ids':[69159,69153,25041]
    })
    assert result != []
    assert result[0]['id'] == 69159
    assert result[1]['id'] == 69153
    assert result[2]['id'] == 25041
