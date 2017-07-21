To use this wrapper

`pip install igdb_api_python`

Example on how to use it

```python
from igdb_api_python import igdb

igdb = igdb("YOUR_KEY")
result = igdb.games(1942)

for game in result:
    print("Retrieved: " + game["name"])
```
