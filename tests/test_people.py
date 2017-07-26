import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singlePeople():
    result = igdb.people(50)
    assert result != []
def test_multiplePeople():
    result = igdb.people({
        'ids':[69159,69153,25041]
    })
    assert result != []
