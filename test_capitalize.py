import pytest, os

from igdb_api_python.igdb import igdb as igdb

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

#print(os.environ['api_key'])
i = igdb(os.environ['api_key'])
