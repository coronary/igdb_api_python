[![Build Status](https://travis-ci.org/igdb/igdb_api_python.svg?branch=master)](https://travis-ci.org/igdb/igdb_api_python)
[![Coverage Status](https://coveralls.io/repos/github/igdb/igdb_api_python/badge.svg?branch=master)](https://coveralls.io/github/igdb/igdb_api_python?branch=master)
[![PyPI version](https://badge.fury.io/py/igdb-api-python.svg)](https://badge.fury.io/py/igdb-api-python)

To use this wrapper

`pip install igdb_api_python`

Example on how to use it

```python
from igdb_api_python.igdb import igdb

igdb = igdb("YOUR_KEY")
result = igdb.games(1942)

for game in result.body:
    print("Retrieved: " + game["name"])
```

[Example.py](https://github.com/igdb/igdb_api_python/blob/master/example.py) for more examples
