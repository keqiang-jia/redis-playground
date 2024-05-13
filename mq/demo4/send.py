import redis

r = redis.Redis(host='172.29.44.161', port=6379, db=0)

stream_name = 'mystream'

r.xadd(stream_name, {'message': 'Hello World'}, maxlen=1000)

print('Sent message to stream: Hello World')
