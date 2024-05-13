import redis

redis_conn = redis.StrictRedis(host='172.29.44.161', port=6379, db=0)

redis_conn.publish('queue', 'Hello World')
