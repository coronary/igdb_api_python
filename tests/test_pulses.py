import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singlePulse():
    result = igdb.pulses(24000)
    assert result != []
def test_multiplePulses():
    result = igdb.pulses({
        'ids':[25040,25047,25000]
    })
    assert result != []
