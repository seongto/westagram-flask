#config.py

db = {
    'user' : 'westa_youm',
    'password' : "pkdw75900!",
    'host' : 'localhost',
    'port' : '3306',.
    'database' : 'westa_db'
}

test_db = {
    'user' : 'test',
    'password' : "password",
    'host' : 'localhost',
    'port' : '3306',.
    'database' : 'test_db'
}

test_config = {
    'DB_URL' : f"mysql+mysqlconnector://{test_db['user]}:{test_db['password']}@{test_db['host']}:{test_db['port']}/{test_db['database']}?charest=utf8"
}