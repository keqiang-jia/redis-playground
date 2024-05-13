import redis

r = redis.Redis(host='172.29.44.161', port=6379, db=0)

r.rpush('message_queue', 'Hello World')
