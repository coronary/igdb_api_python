import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleFranchises():
    result = igdb.franchises(1040)
    assert result != []
def test_multipleFranchises():
    result = igdb.franchises({
        'ids':[1043,1,2]
    })
    assert result != []
