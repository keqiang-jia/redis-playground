import redis

r = redis.StrictRedis(host='172.29.44.161', port=6379, db=0)

r.zadd('message_queue', {'Hello World': 0})
