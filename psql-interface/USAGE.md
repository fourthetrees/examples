# USAGE

The script `psql.py` contains convenience wrappers around
the core functionality of the `psycopg2` python library.

## Example

Below is an example usage of the two main functions of `psql.py`,
the `push` function which uploads a list of rows, and the `execute`
function, which executes an arbitrary SQL string, returning
any values which may be been produced by the command.


```python
In [1]: import psql

In [2]: config = {'user':'username','password':'somepass','table':'testing'}

In [3]: psql.execute(config,"CREATE TABLE testing(col1 INT, col2 INT)")
Out[3]: []

In [4]: psql.push(config,[(123,456),(111,222)])
pushing 2 rows to testing...
push successful.

In [5]: psql.execute(config,"SELECT * FROM testing")
Out[5]: [(123, 456), (111, 222)]

In [6]: psql.execute(config,"DROP TABLE testing")
Out[6]: []

```

We could have supplied an additional `database` field in our
`config` variable.  Since we did not, the script used the
default value of `postgres` as the database.

The core configuration values are `database`, `user`,
`password`, and `host`.  The defaults for these values
are `postgres`, `postgres`, `None`, and `127.0.0.1` respectively.
The `push` function requires the `table` field as well, for
which there is not a default value.


