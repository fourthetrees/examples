#!/usr/bin/env python3

###################################################
############# PSQL Helper Functions ###############
###################################################

# the `psycopg2` dependency can be installed with:
# `$ sudo pip3 install psycopg2`
import psycopg2 as psql


# push a list of rows to a psql table. 
def push(config,rows):
    assert isinstance(rows,list)
    assert isinstance(config,dict)
    if not 'table' in config:
        raise Exception("missing required parameter: 'table'")
    if not rows:
        print('skipping `push`: no rows provided')
        return
    params = get_params(config)
    with psql.connect(**params) as con:
        with con.cursor() as cur:
            ins = ', '.join(('%s' for _ in rows[0]))
            cmd = 'INSERT INTO {} VALUES ({})'.format(config['table'],ins)
            print('pushing {} rows to {}...'.format(len(rows),config['table']))
            cur.executemany(cmd,rows)
    print('push successful.')


# execute an arbitrary SQL command, and return
# its output as python data.
def execute(config,cmd):
    assert isinstance(config,dict)
    assert isinstance(cmd,str)
    params = get_params(config) 
    with psql.connect(**params) as con:
        with con.cursor() as cur:
            cur.execute(cmd)
            try: data = cur.fetchall()
            except Exception as err:
                if 'no results to fetch' in str(err):
                    data = []
                else: raise err
    return data


# helper function for extracting connection parameters
# from the config dict, supplying reasonable defaults
# where such things are appropriate.
def get_params(config): 
    params = {}
    params['host'] = config.get('host','127.0.0.1')
    params['user'] = config.get('user','postgres')
    params['database'] = config.get('database','postgres')
    if 'password' in config:
        params['password'] = config['password']
    return params


